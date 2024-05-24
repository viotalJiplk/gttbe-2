

class AttributesObserver:
    def __init__(self):
        self.observerDict = {
            "init": {},
            "initAll": [],
            "update": {},
            "updateAll": [],
            "delete": {},
            "deleteAll": [],
        }

    def __setattr__(self, name, value):
        if hasattr(self, "observerDict"):
            if hasattr(self, name):
                if hasattr(self.observerDict["update"], name):
                    for x in self.observerDict["update"][name]:
                        x(name, value)
                for x in self.observerDict["updateAll"]:
                    x(name, value)
            else:
                if hasattr(self.observerDict["init"], name):
                    for x in self.observerDict["init"][name]:
                        x(name, value)
                for x in self.observerDict["initAll"]:
                    x(name, value)
        
        super().__setattr__(name, value)
    
    def __delattr__(self, name):
        if hasattr(self, "observerDict"):
            if hasattr(self, name):
                if hasattr(self.observerDict["delete"], name):
                    for x in self.observerDict["delete"][name]:
                        x(name, value)
                for x in self.observerDict["deleteAll"]:
                    x(name, value)
        super().__delattr__(name, value)

    def register(self, function, attrName, observerType):
        if observerType == "init" or observerType == "all":
            if attrName != None:
                self.observerDict["init"][attrName].append(function)
            else:
                self.observerDict["initAll"].append(function)
        if observerType == "update" or observerType == "all":
            if attrName != None:
                self.observerDict["update"][attrName].append(function)
            else:
                self.observerDict["updateAll"].append(function)
        if observerType == "delete" or observerType == "all":
            if attrName != None:
                self.observerDict["delete"][attrName].append(function)
            else:
                self.observerDict["deleteAll"].append(function)