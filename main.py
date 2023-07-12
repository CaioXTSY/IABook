import os
import pdfplumber
from gtts import gTTS
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def extract_text_from_pdf(pdf_path):
    total_text = ""

    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                total_text += page_text

    except Exception as e:
        print(f"Error reading the PDF file: {e}")

    return total_text

def generate_audiobook(text, filename):
    try:
        audiobook = gTTS(text=text, lang='en')
        audiobook.save(filename)
        print(f"Audiobook saved as {filename}")

    except Exception as e:
        print(f"Error generating the audiobook: {e}")

def main():
    while True:
        print("\n*** Menu ***")
        print("1. Generate an audiobook from a PDF")
        print("2. Exit")

        try:
            option = int(input("Choose an option: "))

            if option == 1:
                Tk().withdraw()
                pdf_path = askopenfilename()
                audio_filename = os.path.splitext(os.path.basename(pdf_path))[0] + '.mp3'
                text = extract_text_from_pdf(pdf_path)

                if text:
                    generate_audiobook(text, audio_filename)

            elif option == 2:
                break

            else:
                print("Invalid option")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()