def objectTester(objectToTest, refObject):
    if isinstance(refObject, object):
        for x in refObject:
            if not objectTester(objectToTest[x], refObject):
                return false
    else:
        return isinstance(objectToTest, refObject)