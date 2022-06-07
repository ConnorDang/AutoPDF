######## IMPORTS #########
import sys
import os
import time
#from io import StringIO

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

"""
####### VARIABLES ########
# Get the filename and extension so we can use it for renaming the newly-created file
filename, file_extension = os.path.splitext(sys.argv[1])

# Append "-filled" to the filename and save it in the same place
# This retains the original file so it can be used again with the script
# It also saves the file in the same folder so it's easy to find
filled_out_file = filename + "-filled" + file_extension

# Re-use for any checkboxes
checkbox = "X"

# Information for the form
# Varibles and their names can be changed to anything depending on the form being filled out
# Date of service and date needed by can be a second argument since the rest of the information will stay pretty much the same
dates_of_service = sys.argv[2]
date_needed_by = sys.argv[3]
patient_name = "Hugh"
patient_dob = "01/01/1970"
hospital_name = "Sickbay"
hospital_address = "709 Starfleet Way"
hospital_phone = "123.456.7890"
release_to = "Jacob Salmela"
phone_number = "123.456.7890"
address = "Deck 10, Enterprise D"
date_signed = time.strftime("%d/%m/%Y")

####### FUNCTIONS ########
def main():
    packet = StringIO.StringIO()
    # Create a new PDF with Reportlab
    can = canvas.Canvas(packet, pagesize=letter)

    # This would do better in a loop using some key/value pairs, but this is good enough for government work
    can.drawString(221, 705, patient_name)
    can.drawString(510, 705, patient_dob)
    can.drawString(168, 673, hospital_name)
    can.drawString(168, 650, hospital_address)
    can.drawString(448, 648, hospital_phone)
    can.drawString(237, 608, release_to)
    can.drawString(451, 588, phone_number)
    can.drawString(176, 585, address)
    can.drawString(488, 552, checkbox) # Purpose of release
    can.drawString(301, 508, date_needed_by)
    can.drawString(288, 385, checkbox) # Release method
    can.drawString(299, 480, dates_of_service)
    can.drawString(215, 480, checkbox) # Dates of service checkbox
    can.drawString(163, 406, checkbox) # All health information
    can.drawString(449, 140, date_signed)
    can.drawString(302, 99, checkbox) # Relationship

    # Apply the changes
    can.save()

    # Move to the beginning of the StringIO buffer
    packet.seek(0)
    new_pdf = PdfFileReader(packet)

    # Read the existing PDF (the first argument passed to this script)
    existing_pdf = PdfFileReader(file(filename + file_extension, "rb"))
    output = PdfFileWriter()

    # Add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)

    # Finally, write "output" to a real file
    outputStream = file(filled_out_file, "wb")
    output.write(outputStream)
    outputStream.close()
"""

def main():
    print("Imports Successful")
    pdf = canvas.Canvas("temp.pdf", pagesize = letter)
    pdf.drawString(215, 480, "X")
    pdf.drawString(163, 406, "X")
    pdf.save()





######### SCRIPT #########
if __name__ == "__main__":
    main()