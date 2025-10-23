def mostCommonChar(text):
    text_no_spaces = text.replace(" ", "")
    char_count = {}

    for char in text_no_spaces:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    max_count = 0
    most_common = ""

    for char in text_no_spaces:
        if char_count[char] > max_count:
            max_count = char_count[char]
            most_common = char

    return most_common
