#! python3
import re
import pyperclip

# TODO
#   create a regex for phone numbers
#   create a regex for email addressed
#   get the text off the clipboard
#   extract email/phone numbers from this list
#   copy the extracted email/phone to the clipboard


phone_regex = re.compile(r''
                         r'('  # greate everything as one group so we can loop the tuple later
                         r'((\d\d\d) | (\(\d\d\d\)))?'  # area code with or without (). area code optional
                         r'(\s|-)'  # space or dash
                         r'\d\d\d'
                         r'-'
                         r'\d\d\d\d'  # last 4 digits
                         r'(((ext (\.)?\s) | x)'  # ext optional / extension word part
                         r' (\d{2,5))?'  # extension number-part (optional)
                         r')'  # end first group
                         '', re.VERBOSE)

email_regex = re.compile(r''
                         r'[a-z0-9_.+]+'    # Name. one or more
                         r'@'               # @ symbol
                         r'[a-z0-9_.+]+'    # domain name
                         '', re.VERBOSE | re.IGNORECASE)

text = pyperclip.paste()  # copy text from clipboard

extracted_numbers = phone_regex.findall(text)  # search clipboard for phone numbers using text var

extracted_email = email_regex.findall(text)  # search clipboard for email using text var

all_phone_numbers = []  # since phone numbers are returned as a tuple, we need to append to list

for phone_number in extracted_numbers:  # loop over the extracted_numbers and append them to all_phone_numbers

    # append only the first string in the tuple as extracted_numbers contains a bunch of useless strings
    all_phone_numbers.append(phone_number[0])

results = '\n'.join(all_phone_numbers) + '\n' + '\n'.join(extracted_email)  # prints one email / number per line
pyperclip.copy(results)  # copy updated results to clipboard
