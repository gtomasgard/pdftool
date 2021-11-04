import sys
import os
from PyPDF4 import PdfFileReader, PdfFileWriter
import argparse

def merge_pdfs(paths, output):
    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            # Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))

    # Write out the merged PDF
    with open(output, 'wb') as out:
        pdf_writer.write(out)

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('input', metavar='-in', type=str, nargs='+',
                    help='pdf files to be merged')
    # parser.add_argument('--output', metavar='-o', type=str, nargs=1,
    #                 default='out.pdf', required=False,
    #                 help='the name of the merged pdf')

    args = parser.parse_args()
    cwd = os.getcwd()
    print(cwd)
    merge_pdfs(args.input, output=cwd + '/merged.pdf')


if __name__ == '__main__':
    main()