def mostCommonWord(text):
    words = text.lower().split()
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    max_count = 0
    most_common = ""

    for word in words:
        if word_count[word] > max_count:
            max_count = word_count[word]
            most_common = word

    return most_common
