def transformData(data):
    result = {}
    for item in data:
        item_id = item["id"]
        item_copy = {k: v for k, v in item.items() if k != "id"}
        result[item_id] = item_copy
    return result
