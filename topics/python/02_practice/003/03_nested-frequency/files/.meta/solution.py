def nestedFrequency(nested_list):
    frequency = {}

    for item in nested_list:
        if isinstance(item, list):
            nested_freq = nestedFrequency(item)
            for key, count in nested_freq.items():
                frequency[key] = frequency.get(key, 0) + count
        else:
            frequency[item] = frequency.get(item, 0) + 1

    return frequency
