class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        monotonic_stack = []
        seen = set()
        last_occurrence = {c: i for i, c in enumerate(s)}

        for i, c in enumerate(s):
            if c in seen:
                continue
            while monotonic_stack and c < monotonic_stack[-1] and i < last_occurrence[monotonic_stack[-1]]:
                seen.discard(monotonic_stack.pop())
            seen.add(c)
            monotonic_stack.append(c)

        return ''.join(monotonic_stack)


sol = Solution()
print(sol.removeDuplicateLetters('bcabc'))
print(sol.removeDuplicateLetters('cbacdcbc'))
print(sol.removeDuplicateLetters('leetcode'))
