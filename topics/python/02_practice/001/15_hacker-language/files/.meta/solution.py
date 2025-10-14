def toHackerSpeak(text):
    hacker_map = {"a": "4", "e": "3", "i": "1", "o": "0", "s": "5"}

    result = ""
    for char in text:
        lower_char = char.lower()
        if lower_char in hacker_map:
            result += hacker_map[lower_char]
        else:
            result += char
    return result
