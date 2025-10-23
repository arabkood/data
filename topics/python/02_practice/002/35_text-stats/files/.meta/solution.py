def textStats(text):
    chars = len(text.replace(" ", "").replace("\n", ""))
    words = len(text.split()) if text.strip() else 0
    lines = text.count("\n") + 1
    spaces = text.count(" ")

    return {
        "chars": chars,
        "words": words,
        "lines": lines,
        "spaces": spaces
    }
