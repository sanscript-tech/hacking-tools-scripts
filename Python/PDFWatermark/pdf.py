from reportlab.pdfgen.canvas import Canvas
import PyPDF2

#input pdf
print("Enter the pdf name")
initial_pdf_name=input()

#watermaek text pdf
print("Enter the new pdf name")
new_pdf_name=input()

#watermarktext
print("Enter the watermark text")
watermark_text=input()

#watermark location
print("Enter the location,(ex- 80 90)")
x,y=map(int,input().split())

#create a watermaek text pdf
pdf=Canvas("new.pdf")
pdf.drawString(x,y,watermark_text)
pdf.save()

# open and read the orignal file
first_pdf_file=open(initial_pdf_name,'rb')
first_pdf=PyPDF2.PdfFileReader(first_pdf_file)
count=first_pdf.getNumPages()

# open and read the watermark file
secound_pdf_file=open("new.pdf",'rb')
secound_pdf=PyPDF2.PdfFileReader(secound_pdf_file)

#open and write on the result file
new_pdf_file=_file=open(new_pdf_name,'wb')
new_pdf=PyPDF2.PdfFileWriter()

secound_pdf_page=first_pdf.getPage(0)

#watermark the pdf
for i in range(count):
    first_pdf_page=first_pdf.getPage(i)
    first_pdf_page.mergePage(secound_pdf_page)
    new_pdf.addPage(first_pdf_page)


#close all files
first_pdf_file.close()
secound_pdf_file.close()
new_pdf_file.close()