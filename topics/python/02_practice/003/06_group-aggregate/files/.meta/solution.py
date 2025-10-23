def groupAndSum(items):
    result = {}
    for item in items:
        category = item["category"]
        value = item["value"]
        result[category] = result.get(category, 0) + value
    return result
