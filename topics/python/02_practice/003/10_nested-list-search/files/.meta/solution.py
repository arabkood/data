def findInNested(nested_list, target):
    for item in nested_list:
        if isinstance(item, list):
            if findInNested(item, target):
                return True
        elif item == target:
            return True
    return False
