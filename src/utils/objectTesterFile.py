def objectTester(objectToTest, refObject):
    """Tests if objects are the same

    Args:
        objectToTest (_type_): _description_
        refObject (_type_): _description_

    Returns:
        _type_: _description_
    """
    if isinstance(refObject, object):
        for x in refObject:
            if not objectTester(objectToTest[x], refObject):
                return false
    else:
        return isinstance(objectToTest, refObject)
