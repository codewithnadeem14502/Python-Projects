# Project 4: PDF Merger    

# ReferenceLink : https://pypdf2.readthedocs.io/en/3.0.0/user/merging-pdfs.html#showing-more-merging-options

# Old - Method -1 :  

# new method is below 
# import PyPDF2 

# pdfiles =  ["1.pdf", "2.pdf", "3.pdf"]
# merger = PyPDF2.PdfMerger()
# for pdf in pdfiles:
#     pdfFiles = open(pdf,'rb')
#     pdfReader = PyPDF2.PdfReader(pdfFiles)
#     merger.append(pdf)

# merger.write("merged-pdf.pdf")
# merger.close()

# New - Method -2 : 

# from PyPDF2 import PdfWriter

# merger = PdfWriter()

# for pdf in ["1.pdf", "2.pdf", "3.pdf"]:
#     merger.append(pdf)

# merger.write("NEWmerged-pdf.pdf")
# merger.close()