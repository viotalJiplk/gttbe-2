from pathlib import Path
import os
import importlib
import logging
import colorlog

directory = 'tests/'

def getLogger(name:str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    formatter = colorlog.ColoredFormatter(
        '%(log_color)s%(message)s',
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

defaultLogger = getLogger("default")

def removeExtension(filename: str) -> str:
    return os.path.splitext(filename)[0]

def listModules(directory):
    result = []
    path = Path(directory)
    for file in path.rglob('*.py'):
        if file.is_file():
            result.append(removeExtension(str(file)).replace("/", "."))
    return result

passed = 0
skipped = 0
failed = 0

modules = listModules(directory)
for module in modules:
    try:
        mod = importlib.import_module(module)
    except:
        defaultLogger.error(f"Loading of module `{module}` failed")
        break

    try:
        testCls = mod.Test()
    except:
        defaultLogger.error(f"Initializing of module `{module}` failed")
        skipped += 1
        break

    try:
        testCls.run()
    except Exception as e:
        defaultLogger.error(f"Test `{module}` failed with message: \n {e}")
        failed += 1

    try:
        del testCls
    except:
        defaultLogger.error(f"Destruction of test `{module}` failed")

    defaultLogger.info(f"Test `{module}` succeed")
