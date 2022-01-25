import PyPDF2
import sys

inputs = sys.argv[1:]   # here at the index 0 always the filename
# by doing [1:] it will take all the argument we pass into a list

def pdf_combiner(pdf_list):
    for pdf in pdf_list:
        print(pdf)

pdf_combiner(inputs)