from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        if not nums:
            return ranges
        last = nums[0]
        curr_start = last
        for num in nums[1:]:
            if num == last + 1:
                last = num
            else:
                if curr_start == last:
                    ranges.append(str(last))
                else:
                    ranges.append(str(curr_start) + '->' + str(last))
                last = num
                curr_start = num
        if curr_start == last:
            ranges.append(str(last))
        else:
            ranges.append(str(curr_start) + '->' + str(last))
        return ranges


s = Solution()
print(s.summaryRanges([0, 1, 2, 4, 5, 7]))
print(s.summaryRanges([0, 2, 3, 4, 6, 8, 9]))
