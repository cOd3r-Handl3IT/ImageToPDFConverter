import os
from PIL import Image
from fpdf import FPDF

# Folder paths (without trailing backslash)
image_path = r"C:\Users\Robert\Documents\GitHub\FileConverter"
pdf_path = r"C:\Users\Robert\Documents\GitHub\FileConverter"

# File names
image_file = "egypt_neon_sphinx_pyramid.png"
pdf_file = "egypt_neon_sphinx_pyramid.pdf"

# Compose full file paths
full_image_path = os.path.join(image_path, image_file)
full_pdf_path = os.path.join(pdf_path, pdf_file)
print(f"Image Path: {full_image_path}")
print(f"PDF Path: {full_pdf_path}")

# Get image dimensions dynamically
with Image.open(full_image_path) as img:
    page_width, page_height = img.size  # Match PDF size to image size

# Convert PNG to PDF using FPDF
pdf = FPDF(unit="pt", format=[page_width, page_height])
pdf.add_page()
pdf.image(full_image_path, x=0, y=0, w=page_width, h=page_height)
pdf.output(full_pdf_path)

print(f"PDF saved to: {full_pdf_path} with dimensions {page_width}x{page_height}")