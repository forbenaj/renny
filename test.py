import PyPDF2

class PDFReader:
    def __init__(self, pdf_file_path):
        self.pdf_file_path = pdf_file_path
        self.current_position = 0

    def read_next_1000_letters(self):
        with open(self.pdf_file_path, "rb") as file:
            pdf_reader = PyPDF2.PdfReader(file)
            num_pages = len(pdf_reader.pages)

            letters_count = 0
            text = ""

            while letters_count < 1000 and self.current_position < num_pages:
                page = pdf_reader.pages[self.current_position]
                text += page.extract_text()
                letters_count = len(text)

                if letters_count >= 1000:
                    break

                self.current_position += 1

        return text[:1000], self.current_position

# Example usage:
if __name__ == "__main__":
    pdf_reader = PDFReader("G:/Desktop/Apuntes/MODULO 4.pdf")

    while True:
        letters, next_position = pdf_reader.read_next_1000_letters()
        
        if not letters:
            print("End of document.")
            break
        
        print(letters)
        print("----")

        user_input = input("Press 'Enter' to read the next 1000 letters or 'q' to quit: ")
        if user_input.lower() == "q":
            break

        pdf_reader.current_position = next_position
