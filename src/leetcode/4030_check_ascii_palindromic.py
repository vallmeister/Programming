class Solution:
    def isPalindromic(self, s: str) -> bool:
        ans = []
        for c in s:
            ans.extend(self.get_binary(ord(c)))
        i = 0
        j = len(ans) - 1
        while i < j:
            if ans[i] != ans[j]:
                return False
            i += 1
            j -= 1
        return True

    def get_binary(self, n):
        ans = []
        while n > 0:
            ans.append(n % 2)
            n //= 2
        while len(ans) < 8:
            ans.append(0)
        ans.reverse()
        return ans

s = Solution()
print(s.isPalindromic('ff'))
print(s.isPalindromic('leet'))
