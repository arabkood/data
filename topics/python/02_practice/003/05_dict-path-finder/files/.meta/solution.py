def findPath(nested_dict, target_key):
    if target_key in nested_dict:
        return [target_key]

    for key, value in nested_dict.items():
        if isinstance(value, dict):
            path = findPath(value, target_key)
            if path is not None:
                return [key] + path

    return None
