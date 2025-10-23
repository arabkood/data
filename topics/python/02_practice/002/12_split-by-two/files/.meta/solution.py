def splitByTwo(text):
    if len(text) % 2 != 0:
        text += "_"

    result = []
    for i in range(0, len(text), 2):
        result.append(text[i:i+2])

    return result
