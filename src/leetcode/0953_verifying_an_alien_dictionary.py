def compare_two_strings(str1: str, str2: str, alphabet: dict) -> bool:
    i = 0
    if len(str1) > len(str2) and str1.startswith(str2):
        return False
    while i < len(str1) and i < len(str2):
        if alphabet[str1[i]] < alphabet[str2[i]]:
            return True
        elif alphabet[str1[i]] > alphabet[str2[i]]:
            return False
        i += 1
    return True


def is_alien_sorted(words: list[str], order: str) -> bool:
    alphabet = dict(j for j in zip([i for i in order], [i for i in range(26)]))
    for i in range(1, len(words)):
        if not compare_two_strings(words[i-1], words[i], alphabet):
            return False
    return True


print(is_alien_sorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
print(is_alien_sorted(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"))
print(is_alien_sorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz"))
