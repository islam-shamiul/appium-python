import inspect
import logging


def customeLogger():

    logName = inspect.stack()[1][3]

    logger = logging.getLogger(logName)

    logger.setLevel(logging.DEBUG)

    fileHandeler = logging.FileHandler("{0}.log".format(logName), mode="w")

    fileHandeler.setLevel(logging.DEBUG)

    fileFormatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s : %(message)s', datefmt='%d/%m/%y %I:%M:%S %p %A')

    fileHandeler.setFormatter(fileFormatter)

    logger.addHandler(fileHandeler)

    return logger
