def wordPattern(pattern: str, s: str) -> bool:
    words = s.split()
    if len(words) != len(pattern):
        return False
    pattern_to_word = {}
    word_to_pattern = {}
    for index, c in enumerate(pattern):
        if c in pattern_to_word:
            if pattern_to_word[c] != words[index]:
                return False
        else:
            pattern_to_word[c] = words[index]
    for index, word in enumerate(words):
        if word in word_to_pattern:
            if word_to_pattern[word] != pattern[index]:
                return False
        else:
            word_to_pattern[word] = pattern[index]

    return True


print(wordPattern("abba", "dog cat cat dog"))
print(wordPattern("abba", "dog cat cat fish"))
print(wordPattern("aaaa", "dog cat cat dog"))
