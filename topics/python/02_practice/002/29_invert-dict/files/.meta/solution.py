def invertDict(data):
    inverted = {}

    for key, value in data.items():
        inverted[value] = key

    return inverted
