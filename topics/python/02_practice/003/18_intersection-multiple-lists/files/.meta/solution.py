def intersection(lists):
    if not lists:
        return []

    result = set(lists[0])
    for lst in lists[1:]:
        result = result.intersection(set(lst))

    return list(result)
