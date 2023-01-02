import re


def detectCapitalUse(word: str) -> bool:
    capitals = 0
    for char in word:
        if char.isupper():
            capitals += 1
    return capitals == len(word) or capitals == 0 or (capitals == 1 and word[0].isupper())


def detect_capital_use_with_regex(word: str) -> bool:
    return re.fullmatch(r"[A-Z]*|[a-z]*|[A-Z][a-z]*", word) is not None

print(detectCapitalUse("USA"))
print(detectCapitalUse("FlaG"))
print(detectCapitalUse("leetcode"))
print(detectCapitalUse("Google"))

print(detect_capital_use_with_regex("USA"))
print(detect_capital_use_with_regex("FlaG"))
print(detect_capital_use_with_regex("leetcode"))
print(detect_capital_use_with_regex("Google"))
