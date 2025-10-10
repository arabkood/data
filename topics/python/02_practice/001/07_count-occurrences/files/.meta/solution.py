def countOccurrences(lst, item):
    count = 0
    for element in lst:
        if element == item:
            count += 1
    return count
