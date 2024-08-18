from testUtils import getJws, requestExpect
from copy import deepcopy

class Test:
    def __init__(self):
        self.jws = getJws("114316488057882015")

    def run(self):
        requestExpect.get(f"/backend/page/gg/", 404, {})

    def __del__(self):
        pass
