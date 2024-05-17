import logging
import colorlog

def getLogger(name:str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    formatter = colorlog.ColoredFormatter(
        '%(log_color)s%(levelname)s:%(name)s:%(message)s',
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'bold_red',
        }
    )

    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger