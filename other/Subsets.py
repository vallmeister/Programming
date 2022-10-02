class Solution(object):

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        output = [[]]
        
        for num in nums:
            temp = []
            for element in output:
                ls = element.copy()
                ls += [num]
                temp.append(ls)
            output += temp
        
        return output

s = Solution()

set = [1,2,3,4]
print(s.subsets(set))
