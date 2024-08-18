import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from pathlib import Path
import importlib
import logging
import colorlog
from utils import Server
from utils import resetDb

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

server = Server()

passed = 0
skipped = 0
failed = 0

modules = listModules(directory)
for module in modules:
    name = ".".join(module.split(".")[1:])
    resetDb()
    testFailed = False
    if not server.isRunning():
        defaultLogger.error(f"Server crashed before loading module `{name}`")
        testFailed = True
        break
    try:
        mod = importlib.import_module(module)
    except:
        defaultLogger.error(f"Loading of module `{name}` failed")
        testFailed = True
        continue

    try:
        testCls = mod.Test()
    except:
        defaultLogger.error(f"Initializing of module `{name}` failed")
        skipped += 1
        testFailed = True
        continue

    try:
        testCls.run()
    except Exception as e:
        defaultLogger.error(f"Test `{name}` failed with message: \n  {str(e).replace("\n", "\n  ")}")
        failed += 1
        testFailed = True

    try:
        del testCls
    except:
        defaultLogger.error(f"Destruction of test `{name}` failed")
        testFailed = True
        continue

    if not server.isRunning():
        defaultLogger.error(f"Server crashed after loading module `{name}`")
        testFailed = True
        break

    if not testFailed:
        defaultLogger.info(f"Test `{name}` succeed")
