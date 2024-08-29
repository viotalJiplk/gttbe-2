class AttributesObserver(dict):
    def __init__(self):
        self.__observerDict = {
            "init": {},
            "initAll": [],
            "update": {},
            "updateAll": [],
            "delete": {},
            "deleteAll": [],
            "read": {},
            "readAll": [],
        }

    def __setattr__(self, name, value):
        self.__setitem__(name, value)

    def __setitem__(self, key, value):
        if hasattr(self, "__observerDict"):
            if super().__getitem__(name):
                if hasattr(self.__observerDict["update"], key):
                    for x in self.__observerDict["update"][key]:
                        x(key, value)
                for x in self.__observerDict["updateAll"]:
                    x(key, value)
            else:
                if hasattr(self.__observerDict["init"], key):
                    for x in self.__observerDict["init"][key]:
                        x(key, value)
                for x in self.__observerDict["initAll"]:
                    x(key, value)

        super().__setitem__(key, value)

    def __delattr__(self, name):
        self.__delitem__(name)

    def __delitem__(self, key):
        if hasattr(self, "__observerDict"):
            if super().__getitem__(name):
                if hasattr(self.__observerDict["delete"], key):
                    for x in self.__observerDict["delete"][key]:
                        x(key, value)
                for x in self.__observerDict["deleteAll"]:
                    x(key, value)
        super().__delitem__(key, value)

    def __getattr__(self, name):
        if name == "__observerDict":
            return self.__getattribute__(name)
        try:
            return self.__getitem__(name)
        except KeyError as e:
            raise AttributeError(e.args)

    def __getitem__(self, key):
        if hasattr(self, "__observerDict"):
            if super().__getitem__(key):
                if hasattr(self.__observerDict["read"], key):
                    for x in self.__observerDict["read"][key]:
                        x(key)
                for x in self.__observerDict["readAll"]:
                    x(key)
        return super().__getitem__(key)


    def register(self, function, attrName, observerType):
        if observerType == "init" or observerType == "all":
            if attrName != None:
                self.__observerDict["init"][attrName].append(function)
            else:
                self.__observerDict["initAll"].append(function)
        if observerType == "update" or observerType == "all":
            if attrName != None:
                self.__observerDict["update"][attrName].append(function)
            else:
                self.__observerDict["updateAll"].append(function)
        if observerType == "delete" or observerType == "all":
            if attrName != None:
                self.__observerDict["delete"][attrName].append(function)
            else:
                self.__observerDict["deleteAll"].append(function)
