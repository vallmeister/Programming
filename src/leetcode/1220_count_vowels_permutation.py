from functools import cache


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        MOD = 10 ** 9 + 7

        @cache
        def recursive(vowel, length):
            if length == n:
                return 1
            tmp = 0

            match vowel:
                case 'a':
                    tmp += recursive('e', length + 1)
                case 'e':
                    tmp += recursive('a', length + 1)
                    tmp += recursive('i', length + 1)
                case 'i':
                    for vow in vowels - {'i'}:
                        tmp += recursive(vow, length + 1)
                case 'o':
                    tmp += recursive('i', length + 1)
                    tmp += recursive('u', length + 1)
                case 'u':
                    tmp += recursive('a', length + 1)

            return tmp

        ans = 0
        for v in vowels:
            ans += recursive(v, 1)
        return ans % MOD

    def count_vowel_dp(self, n):
        vowels = {'a', 'e', 'i', 'o', 'u'}
        MOD = 10 ** 9 + 7
        dp = {v: 1 for v in vowels}
        for i in range(2, n + 1):
            new_dp = {}
            new_dp['a'] = dp['e'] + dp['i'] + dp['u']
            new_dp['e'] = dp['a'] + dp['i']
            new_dp['i'] = dp['e'] + dp['o']
            new_dp['o'] = dp['i']
            new_dp['u'] = dp['i'] + dp['o']
            dp = new_dp
        return sum(dp.values()) % MOD


s = Solution()
print(s.countVowelPermutation(1))
print(s.countVowelPermutation(2))
print(s.countVowelPermutation(3))
print(s.countVowelPermutation(5))
