import logging

logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%d/%m/%y %I:%M:%S %p %A', level=logging.DEBUG, filename="logging/test.log", filemode="w")

logging.critical("this is critical msg")
logging.error("this is error msg")
logging.warning("this is warning msg")
logging.info("this is info msg")
logging.debug("this is debug msf")
