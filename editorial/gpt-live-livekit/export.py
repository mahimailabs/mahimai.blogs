"""Derive the optional reader export from the canonical Astro MDX article."""
from pathlib import Path
import re
import shutil

root = Path(__file__).resolve().parents[2]
folder = Path(__file__).resolve().parent / 'delivery'
slug = 'gpt-live-livekit-beyond-first-call'
source = root / 'posts' / f'{slug}.mdx'
_, frontmatter, body = source.read_text().split('---', 2)
frontmatter += f'\ndate: 2026-10-05\nslug: {slug}\ncanonical: https://mahimai.ca/blog/{slug}\nsite_name: Mahimai\nog_image_alt: A visitor speaks to a voice agent while a separate tool system checks a calendar.\n'
body = re.sub(r'^import .*?;\n', '', body, flags=re.M)
body = re.sub(r'<Image .*?/>', '', body)
body = re.sub(r'<ReladrawFigure id="[^"]+" wide={(\w+)} narrow={\w+} alt="([^"]+)" caption="([^"]+)" />', lambda m: f'<figure><img src="{m[1]}.svg" alt="{m[2]}" /><figcaption>{m[3]}</figcaption></figure>', body)
for name in ('architecture', 'correction'):
    body = body.replace('src={' + name + '.src}', f'src="{name}.svg"')
    body = body.replace('width={' + name + '.width}', '')
    body = body.replace('height={' + name + '.height}', '')
    shutil.copyfile(root / 'posts/figures/gpt-live' / f'{name}.svg', folder / f'{name}.svg')
body = body.replace('href={smokeEvidence}', 'href="smoke.json"')
body = re.sub(r'\]\((/[^)]+)\)', r'](https://mahimai.ca\1)', body)
shutil.copyfile(root / 'posts/figures/gpt-live/smoke.json', folder / 'smoke.json')
shutil.copyfile(root / 'posts/covers/gpt-live-livekit-social.jpg', folder / 'hero.jpg')
(folder / f'{slug}.md').write_text('---' + frontmatter + '---' + body)
