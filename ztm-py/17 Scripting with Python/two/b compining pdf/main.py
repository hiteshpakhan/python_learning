import PyPDF2
import sys

inputs = sys.argv[1:]   # here at the index 0 always the filename
# by doing [1:] it will take all the argument we pass into a list

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write("combined.pdf")


pdf_combiner(inputs)

# to run this file :
    # you have to go to the folder location and open the terminal
    # and type the following command
    # python main.py dummy.pdf twopage.pdf wtr.pdf

# it will combine all the pdf you give to it 