# ocr_with_tesseract.py
import fitz              # pip install pymupdf
import pytesseract       # pip install pytesseract
from PIL import Image
import io
import os

# If tesseract is not on PATH, set explicit path:
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

PDF_PATH = "Appointment_Letter_Indranjana_Chatterjee.pdf"
ZOOM = 3    # 2 or 3 -> higher zoom = better OCR, slower

doc = fitz.open(PDF_PATH)
pages_text = []

for i, page in enumerate(doc):
    # render page at higher resolution
    mat = fitz.Matrix(ZOOM, ZOOM)
    pix = page.get_pixmap(matrix=mat, alpha=False)
    img = Image.open(io.BytesIO(pix.tobytes("png")))

    # optional: specify tesseract config for single-column text:
    config = "--psm 3"   # try 3 or 6 depending on layout
    text = pytesseract.image_to_string(img, lang="eng", config=config)
    pages_text.append(text)
    print(f"page {i+1}: {len(text)} chars")

full_text = "\n\n".join(pages_text)
with open("appointment_ocr.txt", "w", encoding="utf-8") as f:
    f.write(full_text)

print("Saved appointment_ocr.txt")
