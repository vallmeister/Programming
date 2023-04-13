from collections import deque


class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        stack = []
        pushed = deque(pushed)
        popped = deque(popped)
        while pushed or popped:
            if pushed:
                if pushed[0] == popped[0]:
                    pushed.popleft()
                    popped.popleft()
                elif stack and stack[-1] == popped[0]:
                    stack.pop()
                    popped.popleft()
                else:
                    stack.append(pushed.popleft())
            else:
                if stack[-1] == popped[0]:
                    stack.pop()
                    popped.popleft()
                else:
                    return False
        return True


s = Solution()
print(s.validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
print(s.validateStackSequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))
