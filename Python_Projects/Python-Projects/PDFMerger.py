from PyPDF2 import PdfWriter

merger=PdfWriter()

# collect
pdfs=[]
count=int(input("how many pdf's you want to merge:"))

for i in range(0,count):
    name_pdf=input("which pdfs you want to merge: ")
    pdfs.append(name_pdf)

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged_pdf.pdf")
merger.close()
