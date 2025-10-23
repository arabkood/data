def removeNthFromEnd(items, n):
    index_to_remove = len(items) - n
    result = []

    for i in range(len(items)):
        if i != index_to_remove:
            result.append(items[i])

    return result
