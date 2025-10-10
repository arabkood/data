def filterNumbers(items):
    result = []
    for item in items:
        if isinstance(item, (int, float)) and not isinstance(item, bool):
            result.append(item)
    return result
