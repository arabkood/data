def charPositions(text):
    positions = {}

    for i, char in enumerate(text):
        if char in positions:
            positions[char].append(i)
        else:
            positions[char] = [i]

    return positions
