from PIL import Image
from fpdf import FPDF

# Load the uploaded image
image_path = "/mnt/data/A_photograph_captures_a_bouquet_of_roses_and_carna.png"
pdf_path = "/mnt/data/Roses_Carnations_Bouquet.pdf"

# Convert PNG to PDF using FPDF
pdf = FPDF(unit="pt", format=[4500, 5400])  # Portrait dimensions
pdf.add_page()
pdf.image(image_path, x=0, y=0, w=4500, h=5400)
pdf.output(pdf_path)
pdf_path
