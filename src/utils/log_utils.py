from importlib.resources import path
import logging


def set_custom_logger():
    global LOGGER

    LOGGER = logging.getLogger(__name__)
    LOGGER.setLevel(logging.INFO)
    log_path = 'logs/'+ __name__ + '_log.txt'
    
    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(logging.ERROR)

    fileHandler = logging.FileHandler(log_path, mode='w')
    fileHandler.setLevel(logging.INFO)

    formatter = logging.Formatter( 
                            '%(asctime)s %(levelname)s File_name: %(filename)s Function_name: %(funcName)s Line_no: %(lineno)d Message: %(message)s' ,datefmt='%d/%m/%Y %I:%M:%S %p')
    consoleHandler.setFormatter(formatter)
    fileHandler.setFormatter(formatter)

    LOGGER.addHandler(fileHandler)
    LOGGER.addHandler(consoleHandler)

    

    return LOGGER


