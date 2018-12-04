import re


def zero_to_one():
    bat_regex = re.compile(r'Bat(wo)?man', re.IGNORECASE)  # the () group can appear 1 or 0 times, hence the ? escape \?
    mo = bat_regex.search("The adventures of batman")
    print(mo.group())

    mo = bat_regex.search("The adventures of Batwoman")
    print(mo.group())


def phone_optional_area():
    phone_regex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')  # are code can now appear once or not at all
    mo = phone_regex.search("My phone number is 555-444-9999. Call me tomorrow")
    mo2 = phone_regex.search("My phone number is 444-9999. Call me tomorrow")
    print(mo.group(), mo2.group())


def zero_or_more():
    bat_regex = re.compile(r'Bat(wo)*man', re.IGNORECASE)  # * means 0 or more times. escape with \*
    mo = bat_regex.search("The adventures of batwowowowoman")
    print(mo.group())


def one_or_more():
    bat_regex = re.compile(r'Bat(wo)+man', re.IGNORECASE)  # + means one or more
    mo = bat_regex.search("The adventures of batwoman")
    print(mo.group())


def exactly():
    ha_regex = re.compile(r'(Ha){3}', re.IGNORECASE)  # exactly 3 times
    mo = ha_regex.search("He said hahaha")
    print(mo.group())

    phone_regex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')

    # would need to allow whitespace to be ignored with ?'s
    mo2 = phone_regex.search("My numbers are 406-9364,541-888-9999,212-555-0000")
    print(mo2.group())


def at_least_at_most():
    redex = re.compile(r'(ha){3,5}', re.IGNORECASE)  # at least 3 at most 5
    mo = redex.search("He said hahahaha")
    print(mo.group())

    redex = re.compile(r'(ha){3,}', re.IGNORECASE)  # at least 3
    mo = redex.search("He said hahahahahahahahahahahahahahahaha")
    print(mo.group())


def find_all():
    resume = """
"Call me at 111-222-3333 tomorrow, or at 444-555-6666 at my office phone any time."
"Call me at 111-222-3333 tomorrow, or at 444-555-6666 at my office phone any time."
"Call me at 111-222-3333 tomorrow, or at 444-555-6666 at my office phone any time."
"Call me at 111-222-3333 tomorrow, or at 444-555-6666 at my office phone any time."
"Call me at 111-222-3333 tomorrow, or at 444-555-6666 at my office phone any time."
"Call me at 111-222-3333 tomorrow, or at 444-555-6666 at my office phone any time."
"Call me at 111-222-3333 tomorrow, or at 444-555-6666 at my office phone any time."
"Call me at 111-222-3333 tomorrow, or at 444-555-6666 at my office phone any time."
"Call me at 111-222-3333 tomorrow, or at 444-555-6666 at my office phone any time."
"Call me at 111-222-3333 tomorrow, or at 444-555-6666 at my office phone any time."
"Call me at 111-222-3333 tomorrow, or at 444-555-6666 at my office phone any time."
"Call me at 111-222-3333 tomorrow, or at 444-555-6666 at my office phone any time."
"Call me at 111-222-3333 tomorrow, or at 444-555-6666 at my office phone any time."
"Call me at 111-222-3333 tomorrow, or at 444-555-6666 at my office phone any time."
"Call me at 111-222-3333 tomorrow, or at 444-555-6666 at my office phone any time."
"Call me at 111-222-3333 tomorrow, or at 444-555-6666 at my office phone any time."
"Call me at 111-222-3333 tomorrow, or at 444-555-6666 at my office phone any time."
"Call me at 111-222-3333 tomorrow, or at 444-555-6666 at my office phone any time."
"Call me at 111-222-3333 tomorrow, or at 444-555-6666 at my office phone any time."
"Call me at 111-222-3333 tomorrow, or at 444-555-6666 at my office phone any time."
"""
    phone_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    mo = phone_regex.findall(resume)
    print(mo)


def find_all_groups():
    resume = """"Call me at 111-222-3333 tomorrow, or at 444-555-6666 at my office phone any time."
"Call me at 111-222-3333 tomorrow, or at 444-555-6666 at my office phone any time."
"Call me at 111-222-3333 tomorrow, or at 444-555-6666 at my office phone any time."
"Call me at 111-222-3333 tomorrow, or at 444-555-6666 at my office phone any time."
"Call me at 111-222-3333 tomorrow, or at 444-555-6666 at my office phone any time."
"Call me at 111-222-3333 tomorrow, or at 444-555-6666 at my office phone any time."
"Call me at 111-222-3333 tomorrow, or at 444-555-6666 at my office phone any time."
"Call me at 111-222-3333 tomorrow, or at 444-555-6666 at my office phone any time."
"Call me at 111-222-3333 tomorrow, or at 444-555-6666 at my office phone any time."
"Call me at 111-222-3333 tomorrow, or at 444-555-6666 at my office phone any time."
"Call me at 111-222-3333 tomorrow, or at 444-555-6666 at my office phone any time."
"Call me at 111-222-3333 tomorrow, or at 444-555-6666 at my office phone any time."
"Call me at 111-222-3333 tomorrow, or at 444-555-6666 at my office phone any time."
"Call me at 111-222-3333 tomorrow, or at 444-555-6666 at my office phone any time."
"Call me at 111-222-3333 tomorrow, or at 444-555-6666 at my office phone any time."
"Call me at 111-222-3333 tomorrow, or at 444-555-6666 at my office phone any time."
"Call me at 111-222-3333 tomorrow, or at 444-555-6666 at my office phone any time."
"Call me at 111-222-3333 tomorrow, or at 444-555-6666 at my office phone any time."
"Call me at 111-222-3333 tomorrow, or at 444-555-6666 at my office phone any time."
"Call me at 111-222-3333 tomorrow, or at 444-555-6666 at my office phone any time."
"""
    phone_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
    mo = phone_regex.findall(resume)
    print(mo)


def create_obj():
    val_regex_obj = re.compile(r'[aeiou]', re.IGNORECASE)  # means or
    message = "qweertyuioplkjhgffddsaaaazxcvbnm"
    mo = val_regex_obj.findall(message)
    print(mo)


def create_negative_obj():
    val_regex_obj = re.compile(r'[^aeiou]', re.IGNORECASE)  # everything except
    message = "qweertyuioplkj hgffddsaaaazxcvbnm"
    mo = val_regex_obj.findall(message)
    print(mo)


def begins_with():
    begins_with_regex = re.compile(r'^Hello')  # ^ has to be at the beginning of the string
    mo = begins_with_regex.search("Hello there!")
    mo2 = begins_with_regex.search("He said Hello")
    print(mo.group())


def end_of():
    ends_with_word = re.compile(r'world!$')  # has to be at the end of the string
    mo = ends_with_word.search("Hello world!")
    print(mo.group())


def all_digits():
    all_digits_regex = re.compile(r'^\d+$')  # has to start with one or more, and end with digit
    mo = all_digits_regex.search("651651651651651651321651651621651635216541651")
    print(mo.group())


def wild_card():
    at_regex = re.compile(r'.at')  # anything followed by at
    mo = at_regex.findall("The cat in the hat sat on the flat mat")
    print(mo)
    at_regex = re.compile(r'.{1,2}at')
    mo = at_regex.findall("The cat in the hat sat on the flat mat")
    print(mo)


def dot_star():
    name_regex = re.compile(r'First Name: (.*) Last Name: (.*)')  # look for First name: . Then what ever comes after
    mo = name_regex.findall("First Name: Jacob Last Name: Rammer")
    print(mo)


def find_replace():
    name_regex = re.compile(r'Agent \w+', re.IGNORECASE)  # Agent followed by one or more letter
    mo = name_regex.findall("Agent Alice gave secret documents to Agent bob.")
    print(mo)

    mo = name_regex.sub('REDACTED', "Agent Alice gave secret documents to Agent bob.")
    print(mo)

    name_regex = re.compile(r'Agent (\w)\w*', re.IGNORECASE)  # One word character, followed by 0+ word characters
    mo = name_regex.sub(r'Agent \1****', "Agent Alice gave secret documents to Agent bob.")  # use text from group one
    print(mo)


def verbose():
    re.compile(r''
               r'\d\d\d'        # area code
               r'-'             # first dash
               r'\d\d\d'        # first three digits
               r'-'             # second dash
               r'\d\d\d\d'      # last 4 digits
               "", re.VERBOSE)
