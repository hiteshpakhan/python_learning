from csv import reader
import PyPDF2

pdf1 = open("dummy.pdf", "r")   #here "r" is the read mode
print(pdf1) #output:- <_io.TextIOWrapper name='dummy.pdf' mode='r' encoding='cp1252'>
# it will give an object as an result

with open("dummy.pdf", "rb") as file:   # rb = read binary  # pdf are in binary form so you have to read it by rb
    reader = PyPDF2.PdfFileReader(file)
    print("this pdf has ",reader.numPages," number of pages")    # it will tell you how many pages the pdf have


pdf2 = open("twopage.pdf", "rb")
read_pdf = PyPDF2.PdfFileReader(pdf2)
print(read_pdf.getPage(0))      # it will read the first page of the pdf # but insure that your mode is rb
# it will give you the hole data in the form of distionary

page1 = read_pdf.getPage(0)
print(page1.rotateClockwise(90)) #it will rotate the page clock wise
print(page1.rotateCounterClockwise(90))  # it will rotate the page counter clock wise

# to save the changed pdf file
page1.rotateClockwise(90)
writer_file = PyPDF2.PdfFileWriter()
writer_file.addPage(page1)
with open("new.pdf", "wb") as new_file:
    writer_file.write(new_file)     #here write will create the new pdf by the name of new.pdf