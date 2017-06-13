def is_anagram(a, b):
    return a.lower() != b.lower() and sorted(a.lower()) == sorted(b.lower())


def detect_anagrams(word, possible_anagrams):
    return [w for w in possible_anagrams if is_anagram(word, w)]