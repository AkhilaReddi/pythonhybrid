import logging
class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="C://Users//aravula2//testpy//pythonhybrid//logs",format ="%(asctime)s: %(leveltime)s: %(message)s',datefmt ='%m/%d%y %I:%M:%S %p")
        logger= logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger