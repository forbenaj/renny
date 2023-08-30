import PyPDF2
import docx

def read_pdf_text(pdf_file_path,index):
    with open(pdf_file_path, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)
        
        result = ""

        pages = pdf_reader.pages
        
        last_page = 0
        next_page = 0

        for page in pages:

            page_text = page.extract_text()
            next_page += len(page_text)
            
            if index < next_page:
                start = index-last_page
                result += page_text[start:start+1000-len(result)]
                index=index+len(result)
                if len(result) >= 1000:
                    break
            else:
                last_page = next_page
                continue
            last_page = next_page


    return result,index

#pdf_file_path = 'C:/Benaj/Desktop/documento de prueba.pdf'
#text_from_pdf,index = read_pdf_text(pdf_file_path,0)

#print(text_from_pdf,index)


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
#docx_file_path = 'G:/Desktop/Apunte_COBOL_Alumnos.docx'
#text_from_docx,index = read_docx_text(docx_file_path,0)

#print(text_from_docx,index)

def read_txt(txt_file,i):

    with open(txt_file,"r", encoding="utf-8") as file:
        text = file.read()

    result = text[i:i+1000]

    return result,i+1000

#print(read_txt("C:/Benaj/Desktop/The Stigma.txt",0))

def extension(filename):
    # Split the filename by '.' to get the parts
    parts = filename.split('.')
    if len(parts) > 1:
        # Return the last part, which is the file extension
        return parts[-1].lower()
    else:
        # If there is no extension, return an empty string
        return ""