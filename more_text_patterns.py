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


at_least_at_most()
