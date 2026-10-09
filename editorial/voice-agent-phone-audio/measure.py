"""Measure WER of a local Whisper model on LibriSpeech audio through each simulated line."""
import io, sys, json
import numpy as np, pyarrow.parquet as pq, soundfile as sf, jiwer
from huggingface_hub import hf_hub_download
from livekit import rtc
sys.path.insert(0, sys.argv[1])
from phone_line import PhoneLine
from faster_whisper import WhisperModel

N = int(sys.argv[2]) if len(sys.argv) > 2 else 30
path = hf_hub_download('hf-internal-testing/librispeech_asr_dummy', 'clean/validation-00000-of-00001.parquet', repo_type='dataset')
rows = pq.read_table(path).to_pylist()[:N]
model = WhisperModel('base.en', device='cpu', compute_type='int8')
norm = jiwer.Compose([jiwer.ToLowerCase(), jiwer.RemovePunctuation(), jiwer.RemoveMultipleSpaces(), jiwer.Strip()])

def through(audio, rate, line, fixes, seed):
    pl = PhoneLine(seed=seed); pl.set_line(line, fixes); pl.note_rate(rate)
    step = rate // 100; out = []
    for i in range(0, len(audio) - step + 1, step):
        f = rtc.AudioFrame(audio[i:i+step].tobytes(), rate, 1, step)
        out += [np.frombuffer(o.data, np.int16) for o in pl.process(f)]
    return np.concatenate(out), pl.stats

conds = [("web", False), ("landline", False), ("cell", False), ("cell", True)]
results = {c: ([], []) for c in conds}
stats = {c: [] for c in conds}
for k, row in enumerate(rows):
    audio, rate = sf.read(io.BytesIO(row['audio']['bytes']), dtype='int16')
    ref = norm(row['text'])
    for c in conds:
        out, st = through(audio, rate, *c, seed=k)
        segs, _ = model.transcribe(out.astype(np.float32) / 32768, language='en', beam_size=1, vad_filter=False)
        hyp = norm(' '.join(s.text for s in segs))
        results[c][0].append(ref); results[c][1].append(hyp); stats[c].append(st)
for c in conds:
    refs, hyps = results[c]
    p = sum(s.packets for s in stats[c]) or 1
    print(json.dumps({"line": c[0], "fixes": c[1], "wer": round(jiwer.wer(refs, hyps), 4),
        "silent_pct": round(100 * sum(s.silent for s in stats[c]) / p, 1),
        "lost_pct": round(100 * sum(s.lost for s in stats[c]) / p, 1),
        "late_pct": round(100 * sum(s.late for s in stats[c]) / p, 1),
        "recovered_pct": round(100 * sum(s.recovered for s in stats[c]) / p, 1),
        "concealed_pct": round(100 * sum(s.concealed for s in stats[c]) / p, 1)}))
