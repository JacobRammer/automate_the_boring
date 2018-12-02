# Not needed on Windows

import sys


# ! python3

# def div_42_by(divide_by):
#     try:
#         return 42 / divide_by
#     except ZeroDivisionError:
#         print("Divide by zero error")
#
#
# print(div_42_by(0))
# print(div_42_by(5000000))
# print(div_42_by(5410515140561))


def num_cats():
    while True:
        try:
            num_cats = input("How many cats do you have: ")
            if len(num_cats) == 0:
                break
            if int(num_cats) >= 4:
                print("That's a lot of cats!")
                break
            else:
                print("That's not that many cats")
        except ValueError:
            print("Integer expected")


num_cats()

# Prints command from run windows. Separated by spaces
print(sys.argv)
exit_console = input("Press enter to continue: ")
