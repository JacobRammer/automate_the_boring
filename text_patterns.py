import re  # import regular expressions

message = "Call me at 111-222-3333 tomorrow, or at 444-555-6666 at my office phone any time."  # message to search

phone_number = re.compile('\d\d\d-\d\d\d-\d\d\d\d')  # pattern to search \d = digit, "-" means dash

number_list = phone_number.findall(message)  # create number_list as a list. will search message for all phone numbers

mo = phone_number.search(message)  # mo for matched object. can be anything. Only returns first match

print(phone_number.findall(message))  # syntax to find all phone_numbers in the string

print("Number list: ", number_list)
for i in number_list:
    # prints phone numbers in message
    print(i)

fin = open("test.txt")  # open text file
file_text = fin.read()  # read the contents of fin. re cannot read the file contents

new_list = phone_number.findall(file_text)  # create new_list as a list containing all phone numbers in file_text

print(new_list)
for i in new_list:
    print(i)


def is_phone_number(text):  # phone number have 12 characters
    """
    inefficient way to see if a string is a phone number
    :param text: str
    :return: True of False
    """
    if len(text) != 12:
        return False  # not phone number sized
    for i in range(0, 3):
        if not text[i].isdigit():
            return False  # no area code
    if text[3] != '-':
        return False  # missing dash
    for i in range(4, 7):
        if not text[i].isdigit():
            return False  # no first 3 digits
    if text[7] != "-":
        return False  # missing dash
    for i in range(8, 12):
        if not text[i].isdigit():
            return False  # missing last 4 digits
    return True
