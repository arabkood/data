def deepMerge(dict1, dict2):
    result = dict1.copy()

    for key, value in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deepMerge(result[key], value)
        else:
            result[key] = value

    return result
