import re  # import regular expressions

message = "Call me at 111-222-3333 tomorrow, or at 444-555-6666 at my office phone any time."  # message to search

phone_number = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # pattern to search \d = digit, "-" means dash. r stands for raw

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


phone_number_area_code = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')  # () created groups
area_code = phone_number_area_code.search("111-222-3333")

print(area_code.group(1))  # prints the area code
print(area_code.group(2))  # prints the number


bat_regex = re.compile(r'Bat(man|mobile|copter|bat)')  # | means or

# if any string matches with bat_regex, such as Batmobile. If not found, it will be nonetype and throw error
bat_mo = bat_regex.search('Batmobile lost a wheel')
print(bat_mo.group())


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
