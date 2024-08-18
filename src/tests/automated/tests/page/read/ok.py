from testUtils import getJws, requestExpect
from copy import deepcopy

read = {
    "name": "about",
    "value": "# test"
}

class Test:
    def __init__(self):
        self.jws = getJws("114316488057882015")

    def run(self):
        requestExpect.get(f"/backend/page/about/", 200, {},  read)

    def __del__(self):
        pass
