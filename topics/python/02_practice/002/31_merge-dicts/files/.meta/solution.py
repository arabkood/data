def mergeDicts(dict1, dict2):
    result = {}

    for key, value in dict1.items():
        result[key] = value

    for key, value in dict2.items():
        result[key] = value

    return result
