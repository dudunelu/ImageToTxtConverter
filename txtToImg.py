import os
import string
import PyPDF2
import os.path
from PIL import Image
from pytesseract import *
pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

print("Welcome to the IMAGE convertor !")

print("What format would you like to convert your image to ? : ")
whatType = input('')
	 
def ImgToText():
    try:
        pictureTxtInput = input('Insert the name of the file: ')
        
        img = Image.open(pictureTxtInput)
        output = pytesseract.image_to_string(img)

        file = open("convert1.txt", "a")
        file.write(output)    	 
    except:
    	print("The file is not an Image. Please choose a valid image!")
    	print('\n')
    	ImgToText()

def ImgToDocx():
	try:
		pictureTxtInput = input('Insert the name of the file you want to convert: ')

		img = Image.open(pictureTxtInput)
		output = pytesseract.image_to_string(img)

		file = open("converted.docx", "a")
		file.write(output)
	
	except:
          print("The file is not an Image. Please choose a valid image!")
          ImgToText()

def PDFtoTEXT():
	try:
		TextInput = input('Insert the name of the PDF you want to convert: ')
		pdfTextInput = open(TextInput, 'rb')
		pdfReader = PyPDF2.PdfFileReader(pdfTextInput)
		
		nrOfPages = pdfReader.numPages
		pageObj = pdfReader.getPage(nrOfPages - 1)
		
		output = pageObj.extractText()
		filePDF = open("pdfConverted.txt", "a")
		filePDF.write(output)
		filePDF.close()
	except: 
		print("The file is not a PDF. Please choose a valid PDF!")

if(whatType == "text"):
	 ImgToText()
if(whatType == "document"):
     ImgToDocx()
if(whatType == "pdf"):
     PDFtoTEXT()
