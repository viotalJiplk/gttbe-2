import subprocess
import os
from .config import config

class Server:
    def __init__(self):
        cwd = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
        command = ["flask", "run", "--host", config.server.host, "--port", config.server.port]
        self.__process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, cwd=cwd, env = dict(os.environ, DBhost= config.db.host,
            DBuser= config.db.user,
            DBpass= config.db.password,
            DBdb= config.db.database))
    def __del__(self):
        if self.__process.poll() is None:
            self.__process.terminate()
            self.__process.wait()

    def isRunning(self):
        return self.__process.poll() is None

    def readLineStdOut(self):
        if self.__process.poll() is not None:
            print(self.__process.communicate())
            raise Exception("Server not running")
        return self.__process.stdout.readline()

    def readLineStdErr(self):
        if self.__process.poll() is not None:
            print(self.__process.communicate())
            raise Exception("Server not running")
        return self.process.stderr.readline()
