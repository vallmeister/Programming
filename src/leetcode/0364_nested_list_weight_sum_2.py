from typing import List


class NestedInteger:
    def __init__(self, value=None):
        pass

    def isInteger(self):
        pass

    def add(self, elem):
        pass

    def setInteger(self, value):
        pass

    def getInteger(self):
        pass

    def getList(self):
        pass


class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        max_depth = max(self.get_depth(nested) for nested in nestedList)
        return sum(self.get_sum(nested, max_depth, 1) for nested in nestedList)

    def get_depth(self, nested):
        ans = 1
        if nested.isInteger():
            return ans
        for nn in nested.getList():
            ans = max(ans, 1 + self.get_depth(nn))
        return ans

    def get_sum(self, nestedList, max_depth, curr_depth):
        weight = max_depth - curr_depth + 1
        if nestedList.isInteger():
            return weight * nestedList.getInteger()
        return sum(self.get_sum(nested, max_depth, curr_depth + 1) for nested in nestedList.getList())
