import traceback
import logging

# logging.basicConfig(level=logging.DEBUG, format= "%(asctime)s - %(levelname)s - %(message)s ")
# Write log info to file
logging.basicConfig(filename="log_file.txt", level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s ")


def box_print(symbol, width, height):
    """
    create a box
    :param symbol:
    :param width:
    :param height:
    :return:
    """
    if len(symbol) != 1:
        raise Exception("symbol needs length of one")
    if (width < 2) or (height < 2):
        raise Exception("width and height need to be greater than or equal to 2")

    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (" " * (width - 2)) + symbol)
    print(symbol * width)


# write error message to text file
# try:
#     raise Exception("This is the error message")
#
# except:
#     error_file = open("log file goes here.txt", "a")
#     error_file.write(traceback.format_exc())
#     error_file.close()
#     print("This traceback info was written to error_log.txt")

market_2nd = {"NS": "green", "EW": "red"}


def switch_lights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == "yellow":
            intersection[key] = "red"
        elif intersection[key] == "red":
            intersection[key] = "green"

    assert "red" in intersection.values(), "Neither light is red!" + str(intersection)


# logging.disable(logging.CRITICAL) disables logging
logging.debug("Start of program")


def factorial(n):
    logging.debug("Start of factorial function (%s)" % n)
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug("i is %s, total is %s" % (i, total))

    logging.debug("Return value is %s" % total)
    return total


logging.debug("Start of program")

print(factorial(5))
