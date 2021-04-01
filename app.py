from PyPDF2 import PdfFileWriter, PdfFileReader

from PyPDF2Highlight import createHighlight, addHighlightToPage

pdfInput = PdfFileReader(open("input.pdf", "rb"))
pdfOutput = PdfFileWriter()

page1 = pdfInput.getPage(0)

highlight = createHighlight(0, 0, 10, 10, {
    "author": "",
    "contents": ""
})

addHighlightToPage(highlight, page1, pdfOutput)

pdfOutput.addPage(page1)

outputStream = open("output.pdf", "wb")
pdfOutput.write(outputStream)
