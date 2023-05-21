class Solution:
    # TODO: Revisit how to do with 1 stack
    def findPermutation(self, s: str) -> list[int]:
        permutation = [1]
        help_stack = []
        number_stack = list(range(len(s) + 1, 1, -1))
        for c in s:
            if c == 'I':
                while help_stack:
                    permutation.append(help_stack.pop())
                permutation.append(number_stack.pop())
            elif c == 'D':
                help_stack.append(permutation.pop())
                permutation.append(number_stack.pop())
        while help_stack:
            permutation.append(help_stack.pop())
        return permutation


sol = Solution()
print(sol.findPermutation("I"))
print(sol.findPermutation("DI"))
print(sol.findPermutation("DDIIDI"))
print(sol.findPermutation("D"))
