class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        ans = []
        i = 0
        while i < n:
            if i < n - 1 and num[i] > num[i + 1] and k > 0:
                k -= 1
            else:
                ans.append(num[i])
            i += 1
        while k > 0:
            ans.pop()
            k -= 1
        return ''.join(ans) if ans else '0'
