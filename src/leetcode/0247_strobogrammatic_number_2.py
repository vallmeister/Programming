from typing import List


class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:

        def find_strobogrammatic(n, rec):
            if n == 1:
                return ['0', '1', '8']
            elif n == 2:
                res = ['11', '69', '88', '96']
                if rec:
                    res.append('00')
                return res
            else:
                nums = find_strobogrammatic(n - 2, rec)
                res = []
                for i in range(len(nums)):
                    num = nums[i]
                    res.append('1' + num + '1')
                    res.append('6' + num + '9')
                    res.append('8' + num + '8')
                    res.append('9' + num + '6')
                return res

        return find_strobogrammatic(n, n > 2)


s = Solution()
print(s.findStrobogrammatic(2))
print(s.findStrobogrammatic(1))
print(s.findStrobogrammatic(3))
print(s.findStrobogrammatic(4))
l1 = s.findStrobogrammatic(6)
print(sorted(l1))
