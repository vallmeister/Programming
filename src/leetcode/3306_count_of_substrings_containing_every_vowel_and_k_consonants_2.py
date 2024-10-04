from collections import defaultdict


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        return self.count_at_least_k_consonants(word, k) - self.count_at_least_k_consonants(word, k + 1)

    def count_at_least_k_consonants(self, word, k):
        vowels = 'aeiou'
        n = len(word)
        vowel_count = defaultdict(int)
        consonant_count = 0
        left = 0
        ans = 0
        for r, char in enumerate(word):
            if char in vowels:
                vowel_count[char] += 1
            else:
                consonant_count += 1
            while len(vowel_count) == 5 and consonant_count >= k:
                ans += n - r
                left_char = word[left]
                if left_char in vowels:
                    vowel_count[left_char] -= 1
                    if vowel_count[left_char] == 0:
                        del vowel_count[left_char]
                else:
                    consonant_count -= 1
                left += 1
        return ans


s = Solution()
print(s.countOfSubstrings("aeioqq", 1))
print(s.countOfSubstrings("iqeaouqi", 2))
