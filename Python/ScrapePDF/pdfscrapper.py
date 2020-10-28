# import PyPDF2 library
import PyPDF2 as p2

pdffile = input("Enter path to pdf file you want to scrape: \n")
PDFfile = open(pdffile, "rb")
pdfread = p2.PdfFileReader(PDFfile)


# to check wheather the pdf is encrypted or not
print(pdfread.getIsEncrypted())
 

# to get information about the document like creator, creation_date
print(pdfread.getDocumentInfo())


# to get number of pages
print(pdfread.getNumPages())


# To extract text from a singl page of pdf
a = int(input("Enter the page no. from which you want to extract text: \n"))
x = pdfread.getPage(a)
print(x.extractText())


# Extract entire pdf
print("---------ENTIRE PDF----------")
i = 0
while i<pdfread.getNumPages():
    pageinfo = pdfread.getPage(i)
    print(pageinfo.extractText())
    i += 1