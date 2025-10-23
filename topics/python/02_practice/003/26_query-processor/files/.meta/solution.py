def queryData(data, query):
    result = []

    for item in data:
        matches = True
        for key, value in query.items():
            if key not in item or item[key] != value:
                matches = False
                break
        if matches:
            result.append(item)

    return result
