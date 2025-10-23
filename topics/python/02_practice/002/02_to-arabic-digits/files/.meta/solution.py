digit_map = {
    "0": "٠",
    "1": "١",
    "2": "٢",
    "3": "٣",
    "4": "٤",
    "5": "٥",
    "6": "٦",
    "7": "٧",
    "8": "٨",
    "9": "٩",
}


def toArabicDigits(text):
    result = ""
    for char in text:
        if char in digit_map:
            result += digit_map[char]
        else:
            result += char
    return result
