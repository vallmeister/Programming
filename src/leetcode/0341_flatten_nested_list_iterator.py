from collections import deque


class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        pass

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        pass

    def getList(self) -> [NestedInteger]:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        pass


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.q = deque()

        def dfs(nest_int):
            if nest_int.isInteger():
                self.q.append(nest_int.getInteger())
            else:
                ls = nest_int.getList()
                for element in ls:
                    dfs(element)

        for nested_integer in nestedList:
            dfs(nested_integer)

    def next(self) -> int:
        return self.q.popleft()

    def hasNext(self) -> bool:
        return bool(self.q)
