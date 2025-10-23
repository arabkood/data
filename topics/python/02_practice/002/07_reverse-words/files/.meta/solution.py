def reverseWords(text):
    words = text.split()
    words.reverse()
    return " ".join(words)
