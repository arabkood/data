def findPairs(numbers, target):
    pairs = []
    seen = set()

    for i in range(len(numbers)):
        complement = target - numbers[i]
        if complement in seen:
            pair = sorted([numbers[i], complement])
            if pair not in pairs:
                pairs.append(pair)
        seen.add(numbers[i])

    return pairs
