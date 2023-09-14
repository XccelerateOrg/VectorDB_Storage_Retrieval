from local_embedder.DB_handler import serialize_document_to_database
import argparse
import os
import glob
import pypdfium2 as pdfium
from tqdm import tqdm


parser = argparse.ArgumentParser()
parser.add_argument("--dir", help="Directory containing knowledge in pdfs")
args = parser.parse_args()

def getAllText(pdf_path: str):
    pdf_doc = pdfium.PdfDocument(pdf_path)
    text = ""
    for page_num in range(len(pdf_doc)):
        text += pdf_doc.get_page(page_num).get_textpage().get_text_range()
    pdf_doc.close()
    return text


def main():
    # Your code here
    pdf_files = glob.glob(os.path.join(args.dir, "**/*.pdf"), recursive=True)
    for pdf in tqdm(pdf_files):
        pdf_text = getAllText(pdf)
        bookName = pdf.strip().split(os.sep)[-1][:-4]
        serialize_document_to_database(pdf_text, bookName)


if __name__ == "__main__":
    main()
