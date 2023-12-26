import sys
from loguru import logger

logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level="INFO")

# Your log statements go here
logger.info("This is an informational message")
logger.warning("This is a warning message")

logger.add("file_{time}.log")

logger.add("file_1.log", rotation="500 MB")    # Automatically rotate too big file
logger.add("file_2.log", rotation="12:00")     # New file is created each day at noon
logger.add("file_3.log", rotation="1 week")    # Once the file is too old, it's rotated

logger.add("file_X.log", retention="10 days")  # Cleanup after some time

logger.add("file_Y.log", compression="zip")    # Save some loved space

logger.info("If you're using Python {}, prefer {feature} of course!", 3.6, feature="f-strings")

@logger.catch
def my_function(x, y, z):
    # An error? It's caught anyway!
    return 1 / (x + y + z)

logger.add(sys.stdout, colorize=True, format="<green>{time}</green> <level>{message}</level>")

logger.add("somefile.log", enqueue=True)

# Caution, "diagnose=True" is the default and may leak sensitive data in prod
logger.add("out.log", backtrace=True, diagnose=True)

def func(a, b):
    return a / b

def nested(c):
    try:
        func(5, c)
    except ZeroDivisionError:
        logger.exception("What?!")

nested(0)