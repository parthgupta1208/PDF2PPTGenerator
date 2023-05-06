import PyPDF2

def pdf2text(filename):
# Read the PDF file
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFileObj)
    page_text = []
    for page in range(len(pdfReader.pages)):
        page_text.append(pdfReader.pages[page].extract_text())

    # Print the summary
    return(page_text)