from typing import List


class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:

        def find_strobogrammatic(n):
            if n == 1:
                return ['0', '1', '8']
            elif n == 2:
                res = ['11', '69', '88', '96', '00']
                return res
            else:
                nums = find_strobogrammatic(n - 2)
                res = []
                for i in range(len(nums)):
                    num = nums[i]
                    res.append('1' + num + '1')
                    res.append('6' + num + '9')
                    res.append('8' + num + '8')
                    res.append('9' + num + '6')
                    res.append('0' + num + '0')
                return res

        ans = find_strobogrammatic(n)
        return list(filter(lambda x: not (x.startswith('0') and len(x) > 1), ans))


s = Solution()
print(s.findStrobogrammatic(2))
print(s.findStrobogrammatic(1))
print(s.findStrobogrammatic(3))
print(s.findStrobogrammatic(4))
l1 = s.findStrobogrammatic(6)
print(sorted(l1))
