def flattenList(nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flattenList(item))
        else:
            result.append(item)
    return result
