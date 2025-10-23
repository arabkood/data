def textSimilarity(text1, text2):
    words1 = set(text1.lower().split())
    words2 = set(text2.lower().split())

    common = len(words1.intersection(words2))
    total = len(words1) + len(words2)

    if total == 0:
        return 0.0

    return (common * 2 / total) * 100
