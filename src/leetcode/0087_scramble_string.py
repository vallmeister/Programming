from functools import cache


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:

        @cache
        def memo(st1, st2):
            if not sorted(st1) == sorted(st2):
                return False
            elif len(st1) == 1:
                return True

            for i in range(1, len(st1)):
                no_scramble = memo(st1[:i], st2[:i]) and memo(st1[i:], st2[i:])
                scramble = memo(st1[-i:], st2[:i]) and memo(st1[:-i], st2[i:])
                if scramble or no_scramble:
                    return True
            return False

        return memo(s1, s2)


s = Solution()
print(s.isScramble(s1="great", s2="rgeat"))
print(s.isScramble(s1="abcde", s2="caebd"))
print(s.isScramble(s1="a", s2="a"))
