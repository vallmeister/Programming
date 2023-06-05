class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        strobo_numbers = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        i = 0
        j = len(num) - 1
        while i <= j:
            if num[i] not in strobo_numbers or num[j] not in strobo_numbers:
                return False
            if strobo_numbers[num[i]] != num[j]:
                return False
            i += 1
            j -= 1
        return True


s = Solution()
print(s.isStrobogrammatic('69'))
print(s.isStrobogrammatic('88'))
print(s.isStrobogrammatic('962'))
print(s.isStrobogrammatic('2'))
