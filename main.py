######## IMPORTS #########
from tarfile import GNUTYPE_LONGNAME
import PyPDF2
import time
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


# Import in GIMP as 1.000 pixels/pt - 612 x 792 pts
# GIMP uses bottom-left origin. Canvas uses top-left as origin.
# Helper function to compute Canvas Y
def trueY (GIMP_Y) :
    return 792 - GIMP_Y

def main():

    ### VARIABLES
    GUY = "Sean Dang"

    pdf = canvas.Canvas("temp.pdf", pagesize = letter)
    # Header Section
    pdf.drawString(39, trueY(95), "534")
    pdf.drawString(196, trueY(95), "12")
    pdf.drawString(273, trueY(95), "12/05/2020")
    pdf.drawString(420, trueY(95), "X")
    pdf.drawString(35, trueY(130), "350119")
    pdf.drawString(190, trueY(130), "Menoa Aghajani")
    pdf.drawString(423, trueY(130), "FPEA II")

    # Mid Section
    pdf.drawString(450, trueY(236), GUY)
    pdf.drawString(116, trueY(267), "9135 Tampa Avenue")
    pdf.drawString(495, trueY(267), "F20-01526")
    pdf.drawString(80, trueY(310), "1000 HOURS ON 12/05/20")
    pdf.drawString(375, trueY(310), "1200 HOURS ON 12/05/20")
    pdf.drawString(125, trueY(355), "2.0")

    pdf.save()
    print("Layer Created.")
    time.sleep(2)

    # Add as watermark.
    blankFile = "blank.pdf"
    watermark = "temp.pdf"
    mergeFile = "merged.pdf"

    input_file = open(blankFile,'rb')
    input_pdf = PyPDF2.PdfReader(input_file)

    watermark_file = open(watermark,'rb')
    watermark_pdf = PyPDF2.PdfReader(watermark_file)

    pdf_page = input_pdf.pages[0]
    watermark_page = watermark_pdf.pages[0]

    pdf_page.merge_page(watermark_page)

    output = PyPDF2.PdfWriter()
    output.add_page(pdf_page)
    merged_file = open(mergeFile,'wb')
    output.write(merged_file)

    merged_file.close()
    watermark_file.close()
    input_file.close()

    print("Layer Written Successfully.")


######### SCRIPT #########
if __name__ == "__main__":
    main()