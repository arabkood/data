def areAnagrams(word1, word2):
    # Remove spaces and convert to lowercase
    word1_clean = word1.replace(" ", "").lower()
    word2_clean = word2.replace(" ", "").lower()

    # Check if lengths are different
    if len(word1_clean) != len(word2_clean):
        return False

    # Sort the characters and compare
    return sorted(word1_clean) == sorted(word2_clean)
