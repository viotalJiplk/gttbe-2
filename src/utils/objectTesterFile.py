def objectTester(objectToTest, refObject):
    """Tests if objects are the same

    Args:
        objectToTest (Object): _description_
        refObject (Object): _description_

    Returns:
        bool: _description_
    """
    if isinstance(refObject, object):
        for x in refObject:
            if not objectTester(objectToTest[x], refObject):
                return False
    else:
        return isinstance(objectToTest, refObject)
