from pdfminer.high_level import extract_text
import re
import argparse

# Create a parser
parser = argparse.ArgumentParser(description="Extract email addresses from a pdf file.")

# Add the arguments
parser.add_argument('file_name', metavar='file_name', type=str, help="File name to parse")
parser.add_argument('-d', '--delimiter', default=",", help="Delimiter after each email address")


# Parse the pdf
def parse_pdf():

    # Parse the arguments
    args = parser.parse_args()

    # Extract all text from the pdf and
    # define a regular expression
    text = extract_text(args.file_name)
    mail_addresses = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', text)

    # Write the email addresses to stout and to a file
    with open(f"{args.file_name.split('.')[0]}.txt", 'w') as writer:
        for index, mail in enumerate(mail_addresses):
            if index is not len(mail_addresses)-1:
                writer.write(mail)
                writer.write(f"{args.delimiter}\n")
                print(f"{mail}{args.delimiter}")
            else:
                writer.write(f"{mail}\n")
                print(mail)


# Execute the method
if __name__ == '__main__':
    parse_pdf()
