def count_letters(s: str) -> list[int]:
    letters = [0] * 26
    for letter in s:
        letters[ord(letter) - 97] += 1
    return letters


def compare_letters(l1: list[int], l2: list[int]) -> bool:
    for i in range(26):
        if l1[i] != l2[i]:
            return False
    return True


def check_inclusion(s1: str, s2: str) -> bool:
    s1_letters_count = count_letters(s1)
    n = len(s1)
    s2_curr_letters = count_letters(s2[0:n])
    i = 0
    while i + n < len(s2):
        if compare_letters(s1_letters_count, s2_curr_letters):
            return True
        s2_curr_letters[ord(s2[i]) - 97] -= 1
        s2_curr_letters[ord(s2[i + n]) - 97] += 1
        i += 1
    return compare_letters(s1_letters_count, s2_curr_letters)


print(check_inclusion("ab", "eidbaooo"))
print(check_inclusion("ab", "eidboaoo"))
print(check_inclusion("adc", "dcda"))
