class Solution:
    def minimumOperations(self, num: str) -> int:
        targets = {'00', '25', '50', '75'}
        n = len(num)
        if n < 3:
            if num in targets:
                return 0
            elif '0' in num:
                return 1
            else:
                return n
        min_operations = n - 1 if '0' in num else n
        for i in range(n - 1):
            for j in range(i + 1, len(num)):
                val = num[i] + num[j]
                if val in targets:
                    min_operations = min(min_operations, n - i - 2)
        return min_operations


s = Solution()
print(s.minimumOperations("2245047"))
print(s.minimumOperations("2908305"))
print(s.minimumOperations('10'))
print(s.minimumOperations("444937979672347396583725074143"))
print(s.minimumOperations("820366"))
