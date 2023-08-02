import PyPDF2
import docx

def read_pdf_text(pdf_file_path):
    with open(pdf_file_path, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)

        # Initialize an empty string to store the text content
        #pdf_text = pdf_reader.pages[0].extract_text()
        pdf_text = ""
        pages = pdf_reader.pages
        for page in range(len(pages)):
            pdf_text+=pages[page].extract_text()


    return pdf_text

# Replace 'path/to/your/pdf/file.pdf' with the actual file path.
pdf_file_path = 'G:/Desktop/Apuntes/MODULO 4.pdf'
text_from_pdf = read_pdf_text(pdf_file_path)

print(text_from_pdf)


def read_docx_text(docx_file_path,i):
    doc = docx.Document(docx_file_path)

    # Initialize an empty string to store the text content
    docx_text = ""
    textLength = 0
    # Loop through each paragraph and extract text
    while textLength < 1000:
        paragraph_text = doc.paragraphs[i].text
        if paragraph_text != "":
            docx_text += paragraph_text + "\n"
            textLength += len(paragraph_text)
        i+=1

    return docx_text, i

# Replace 'path/to/your/docx/file.docx' with the actual file path.
docx_file_path = 'G:/Desktop/Apunte_COBOL_Alumnos.docx'
text_from_docx,index = read_docx_text(docx_file_path,0)

#print(text_from_docx,index)