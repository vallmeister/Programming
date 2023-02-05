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


def find_anagrams(s: str, p: str) -> list[int]:
    result = []
    p_letters = count_letters(p)
    n = len(p)
    s_window = count_letters(s[:n])
    i = 0
    while i + n <= len(s):
        if compare_letters(p_letters, s_window):
            result.append(i)
        if i + n >= len(s):
            break
        s_window[ord(s[i]) - 97] -= 1
        s_window[ord(s[i + n]) - 97] += 1
        i += 1
    return result


print(find_anagrams("cbaebabacd", "abc"))
print(find_anagrams("abab", "ab"))
