def findLongestWord(sentence):
    if sentence == "":
        return ""

    words = sentence.split()
    if len(words) == 0:
        return ""

    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest
