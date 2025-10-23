def rotateList(items, n):
    if len(items) == 0:
        return items

    n = n % len(items)

    return items[-n:] + items[:-n]
