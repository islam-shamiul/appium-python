import logging
import customLogger as cl


class customLoggerDemo():

    log = cl.customeLogger()

    def methodOne(self):
        self.log.critical("This is a critical")
        self.log.error("This is a error msg")
        self.log.warning("Warn msg")
        self.log.info("Info msg")
        self.log.debug("Debug msg")

    def methodTwo(self):
        m2 = cl.customeLogger()
        m2.critical("Critical Msg")
        m2.error("Error msg")
        m2.warning("Warn msg")
        m2.info("Info msg")
        m2.debug("Debug msg")


cld = customLoggerDemo()
cld.methodOne()
cld.methodTwo()
