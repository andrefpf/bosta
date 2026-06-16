from pathlib import Path

import fitz  # PyMuPDF


def svg_to_png(input_path: Path, output_path: Path, dpi=300):
    doc = fitz.open(input_path)
    page = doc.load_page(0)
    pix = page.get_pixmap(dpi=dpi, alpha=True)
    pix.save(output_path)
    doc.close()


svg_base_path = Path("data/svg/")
png_base_path = Path("data/png/")

for svg_path in svg_base_path.glob("*.svg"):
    png_path = png_base_path / svg_path.with_suffix(".png").name
    svg_to_png(svg_path, png_path)
