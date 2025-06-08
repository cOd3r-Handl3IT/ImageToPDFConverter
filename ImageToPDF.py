import os
from PIL import Image
from fpdf import FPDF

# Folder paths (without trailing backslash)
image_path = r"C:\Users\Robert\Documents\GitHub\FileConverter"
pdf_path = r"C:\Users\Robert\Documents\GitHub\FileConverter"

# File names
image_file = "A_photograph_captures_a_bouquet_of_roses_and_carna.png"
pdf_file = "Roses_Carnations_Bouquet.pdf"

# Compose full file paths
full_image_path = os.path.join(image_path, image_file)
full_pdf_path = os.path.join(pdf_path, pdf_file)

# Toggle: Set True for Landscape; False for Portrait
is_landscape = False

# Set dimensions based on orientation toggle
if is_landscape:
    page_width, page_height = 5400, 4500
else:
    page_width, page_height = 4500, 5400

# Convert PNG to PDF using FPDF with specified dimensions in points
pdf = FPDF(unit="pt", format=[page_width, page_height])
pdf.add_page()
pdf.image(full_image_path, x=0, y=0, w=page_width, h=page_height)
pdf.output(full_pdf_path)
print(f"PDF saved to: {full_pdf_path} with {'Landscape' if is_landscape else 'Portrait'} orientation")