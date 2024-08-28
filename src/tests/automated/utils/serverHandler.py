import subprocess
import os
import sys
from .config import config
from threading  import Thread
from queue import Queue, Empty

class ReadNonBlocking:
    def __init__(self, pipe):
        self.__queue = Queue()
        self.__thread = Thread(target=self.__enqueueOutput, args=(pipe, self.__queue), daemon=True)
        self.__thread.start()

    def __enqueueOutput(self, out, queue):
        for line in iter(out.readline, b''):
            queue.put(line)
        out.close()

    def readNonBlocking(self):
        result = ""
        while True:
            try:  line = self.__queue.get_nowait()
            except Empty:
                break
            else:
                result += f"\n{line}"
        return result

class Server:
    def __init__(self):
        cwd = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
        command = ["flask", "run", "--host", config.server.host, "--port", config.server.port]
        self.onPosix = 'posix' in sys.builtin_module_names
        self.__process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, cwd=cwd, bufsize=1, close_fds=self.onPosix, env = dict(os.environ, DBhost= config.db.host,
            DBuser= config.db.user,
            DBpass= config.db.password,
            DBdb= config.db.database))
        self.__nonBlockingStdOut = ReadNonBlocking(self.__process.stdout)
        self.__nonBlockingStdErr = ReadNonBlocking(self.__process.stderr)

    def __del__(self):
        if self.__process.poll() is None:
            self.__process.terminate()
            self.__process.wait()

    def isRunning(self):
        return self.__process.poll() is None

    def readStdOutNonBlocking(self):
        return self.__nonBlockingStdOut.readNonBlocking()

    def readStdErrNonBlocking(self):
        return self.__nonBlockingStdErr.readNonBlocking()

    def readLineStdOut(self):
        if self.__process.poll() is not None:
            print(self.__process.communicate())
            raise Exception("Server not running")
        return self.__process.stdout.readline()

    def readLineStdErr(self):
        if self.__process.poll() is not None:
            print(self.__process.communicate())
            raise Exception("Server not running")
        return self.__process.stderr.readline()
