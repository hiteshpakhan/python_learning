from re import template
import PyPDF2

template = PyPDF2.PdfFileReader(open("combined.pdf", "rb")) #this is the shortest way to make file readble

watermark_pdf = PyPDF2.PdfFileReader(open("wtr.pdf", "rb")) #this is our watermark pdf

output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()): #getNumPages will give you the number pages any pdf have
    page = template.getPage(i)
    page.mergePage(watermark_pdf.getPage(0))
    output.addPage(page)

    
with open("watermarked_output.pdf", "wb") as file:
    output.write(file)
