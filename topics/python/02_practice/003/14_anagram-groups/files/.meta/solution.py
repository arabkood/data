def groupAnagrams(strs):
    anagram_dict = {}

    for s in strs:
        sorted_s = "".join(sorted(s))
        if sorted_s not in anagram_dict:
            anagram_dict[sorted_s] = []
        anagram_dict[sorted_s].append(s)

    return list(anagram_dict.values())
