from csv import reader
import PyPDF2

pdf1 = open("dummy.pdf", "r")   #here "r" is the read mode
print(pdf1) #output:- <_io.TextIOWrapper name='dummy.pdf' mode='r' encoding='cp1252'>
# it will give an object as an result

with open("dummy.pdf", "rb") as file:   # rb = read binary  # pdf are in binary form so you have to read it by rb
    reader = PyPDF2.PdfFileReader(file)
    print("this pdf has ",reader.numPages,"number of pages")    # it will tell you how many pages the pdf have

read_pdf = PyPDF2.PdfFileReader(pdf1)
print(read_pdf.getPage(0))      # it will read the first page of the pdf

