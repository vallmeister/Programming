class Solution:
    def minOperations(self, s: str) -> int:

        def alternate(t, prev):
            ans = 0
            for letter in t:
                if letter == prev:
                    ans += 1
                    prev = str(1 - int(letter))
                else:
                    prev = letter
            return ans

        return min(alternate(s, '0'), alternate(s, '1'))


sol = Solution()
print(sol.minOperations("0100"))
print(sol.minOperations("10"))
print(sol.minOperations("1111"))
