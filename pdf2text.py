import PyPDF2

# Read the PDF file
pdfFileObj = open('C:\Everything\AICTEReport_4NM20AI032_ParthGupta.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(pdfFileObj)
text = ''
for page in range(len(pdfReader.pages)):
    text += pdfReader.pages[page].extract_text()

# Generate the summary using TextRank algorithm

# Print the summary
print(text)