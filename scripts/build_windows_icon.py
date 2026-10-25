#!/usr/bin/env python3
"""Generate the Windows ICO from the official transparent VMRX logo.

Requires Pillow: python -m pip install Pillow
Never substitutes a generic logo and fails if original alpha is missing.
"""
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
source = ROOT / "assets" / "vmrx-logo.png"
target = ROOT / "assets" / "vmrx.ico"
if not source.is_file():
    raise SystemExit(f"Official VMRX logo not found: {source}")
with Image.open(source) as original:
    original.load()
    if original.format != "PNG" or original.mode != "RGBA":
        raise SystemExit("VMRX logo must be a transparent RGBA PNG")
    if original.width < 256 or original.height < 256:
        raise SystemExit("VMRX logo resolution must be at least 256x256")
    for point in [(0, 0), (0, original.height - 1), (original.width - 1, 0), (original.width - 1, original.height - 1)]:
        if original.getpixel(point)[3] != 0:
            raise SystemExit(f"VMRX logo background is not transparent: {point}")
    original.save(target, format="ICO",
                  sizes=[(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])
with Image.open(target) as icon:
    if icon.format != "ICO":
        raise SystemExit("ICO generation failed")
print(f"VMRX official Windows icon generated: {target} ({target.stat().st_size:,} bytes)")
