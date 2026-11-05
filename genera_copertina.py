"""Genera copertina blog Centro Risarcimenti.
Uso: python3 cover.py "Categoria" "Titolo" output.webp
"""
import sys, textwrap
from PIL import Image, ImageDraw, ImageFont

cat, title, out = sys.argv[1], sys.argv[2], sys.argv[3]
W, H = 1200, 630
NAVY = (15, 34, 54)
ACCENT = {"Incidenti Stradali": (230, 126, 34), "Malasanità": (46, 160, 140),
          "Infortuni sul Lavoro": (230, 180, 40), "Responsabilità Civile": (90, 140, 220)}.get(cat, (46, 160, 140))

img = Image.new("RGB", (W, H), NAVY)
d = ImageDraw.Draw(img)
# fasce decorative
for i in range(0, 14):
    d.ellipse([W - 420 + i * 18, -260 + i * 18, W + 380 - i * 18, 540 - i * 18],
              outline=tuple(min(255, c + 8 + i * 2) for c in NAVY), width=2)
d.rectangle([0, H - 14, W, H], fill=ACCENT)
d.rectangle([70, 90, 76, 150], fill=ACCENT)

f_cat = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 30)
f_tit = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", 58)
f_brand = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 28)
f_sub = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)

d.text((96, 104), cat.upper(), font=f_cat, fill=ACCENT)
lines = textwrap.wrap(title, width=30)[:4]
y = 190
for ln in lines:
    d.text((70, y), ln, font=f_tit, fill=(255, 255, 255))
    y += 74
d.text((70, H - 90), "CENTRO RISARCIMENTI", font=f_brand, fill=(255, 255, 255))
bx = 70 + d.textlength("CENTRO RISARCIMENTI", font=f_brand) + 28
d.text((bx, H - 86), "Dal 2009 · Consulenza gratuita", font=f_sub, fill=(170, 185, 200))
img.save(out, "WEBP", quality=85)
print(out)
