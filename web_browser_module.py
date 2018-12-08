import webbrowser
import sys
import pyperclip

# check if command line arguments are passed
if len(sys.argv) > 1:  # if command line has arguments
    # ['web_browser_module.py', '870', 'Valencia', 'St.']
    address = " ".join(sys.argv[1:])  # join on space from the start of the address
else:  # no command line arguments, copy from clipboard
    address = pyperclip.paste()

# https://www.google.com/maps/place/<ADDRESS>
webbrowser.open("https://www.google.com/maps/place/" + address)
