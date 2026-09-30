"""Editorial fixtures; run with Python 3.12, torch/torchaudio 2.8.0 on CPU.

uv run --no-project --python 3.12 --with torch==2.8.0 --with torchaudio==2.8.0 python verify-channel.py
"""
import audioop
import json
import math
import sys

import torch
import torchaudio
import torchaudio.functional as AF

# Same two TorchAudio operations used by handset-bench at revision
# 651ce772ba08ab56dd1b057d3b2ac9304c6eeb4a (codec.py).
def reference_roundtrip(x):
    return AF.mu_law_decoding(AF.mu_law_encoding(x, 256), 256).float()


def rms(x):
    return x.square().mean().sqrt()


def measure(frequency, qs, dtype=torch.float64):
    sr = 24000
    t = torch.arange(sr, dtype=dtype) / sr
    x = 0.1 * torch.sin(2 * math.pi * frequency * t)
    y = x
    for q in qs:
        y = AF.lowpass_biquad(y, sr, 3400, Q=q)
    return float(20 * torch.log10(rms(y[sr // 2 :]) / rms(x[sr // 2 :])))


class MuLawSTE(torch.autograd.Function):
    @staticmethod
    def forward(ctx, x):
        return reference_roundtrip(x)

    @staticmethod
    def backward(ctx, grad_output):
        return grad_output


torch.manual_seed(17)
qs = [1 / (2 * math.cos((2 * k + 1) * math.pi / 16)) for k in range(4)]
out = {
    "runtime": {"python": sys.version, "torch": torch.__version__, "torchaudio": torchaudio.__version__, "device": "cpu"},
    "fixture": {"sample_rate": 24000, "tone_seconds": 1, "amplitude": 0.1, "discard_seconds": 0.5, "lowpass_hz": 3400},
    "qs": qs,
    "lowpass_db": {},
}
for dtype in [torch.float32, torch.float64]:
    out["lowpass_db"][str(dtype)] = {
        str(f): {"single": measure(f, [1 / math.sqrt(2)], dtype), "butterworth8": measure(f, qs, dtype), "repeated_q": measure(f, [1 / math.sqrt(2)] * 4, dtype)}
        for f in [3400, 6000]
    }

out["torchaudio_zero"] = {
    "encoded": int(AF.mu_law_encoding(torch.tensor([0.0]), 256)[0]),
    "decoded": float(AF.mu_law_decoding(torch.tensor([128]), 256)[0]),
}
out["pcmu_zero"] = {
    "encoded_hex": audioop.lin2ulaw(bytes(2), 2).hex(),
    "decoded_int16": int.from_bytes(audioop.ulaw2lin(bytes([255]), 2), byteorder=sys.byteorder, signed=True),
}

# Dense near-zero values are intentional: uniform [-1,1] tests can miss cancellation.
x = torch.cat([torch.rand(1_000_000) * 2 - 1, torch.linspace(-0.001, 0.001, 1_000_001)]).requires_grad_(True)
exact = reference_roundtrip(x)
arithmetic_ste = x + (exact - x).detach()
new_ste = MuLawSTE.apply(x)
different = arithmetic_ste != exact
indices = different.nonzero().flatten()
out["ste"] = {
    "tested_samples": x.numel(),
    "arithmetic_mismatches": int(different.sum()),
    "arithmetic_max_abs_error": float((arithmetic_ste - exact).abs().max().detach()),
    "custom_forward_equal": bool(torch.equal(new_ste, exact)),
    "first_mismatch": None if not indices.numel() else {
        "x": float(x[indices[0]].detach()), "exact": float(exact[indices[0]]), "arithmetic": float(arithmetic_ste[indices[0]].detach())
    },
}
new_ste.sum().backward()
out["ste"]["custom_gradient_all_ones"] = bool(torch.equal(x.grad, torch.ones_like(x)))

# The written sign/abs formula has an autograd convention at exactly zero.
zero = torch.tensor([0.0], requires_grad=True)
companded = torch.sign(zero) * torch.log1p(255 * zero.abs()) / math.log(256)
companded.sum().backward()
out["compand_gradient_at_zero"] = float(zero.grad[0])
print(json.dumps(out, indent=2))
