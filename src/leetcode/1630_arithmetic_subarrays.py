from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        m = len(l)
        ans = []
        for i in range(m):
            left = l[i]
            right = r[i] + 1
            if left + 1 == right:
                ans.append(False)
                continue
            subarray = []
            for j in range(left, right):
                subarray.append(nums[j])
            subarray.sort()
            diff = subarray[1] - subarray[0]
            curr = subarray[0]
            for num in subarray[1:]:
                if num - curr != diff:
                    ans.append(False)
                    break
                curr = num
            else:
                ans.append(True)
        return ans


s = Solution()
print(s.checkArithmeticSubarrays([4, 6, 5, 9, 3, 7], l=[0, 0, 2], r=[2, 3, 5]))
print(s.checkArithmeticSubarrays([-12, -9, -3, -12, -6, 15, 20, -25, -20, -15, -10], l=[0, 1, 6, 4, 8, 7],
                                 r=[4, 4, 9, 7, 9, 10]))
