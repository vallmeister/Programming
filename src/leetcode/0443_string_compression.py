from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        chars.append('*')
        char = chars[0]
        count = 1
        idx = 0
        for i in range(1, len(chars)):
            if chars[i] == char:
                count += 1
            else:
                chars[idx] = char
                idx += 1
                stack = []
                if count > 1:
                    while count > 0:
                        stack.append(count % 10)
                        count //= 10
                    while stack:
                        chars[idx] = str(stack.pop())
                        idx += 1
                char = chars[i]
                count = 1
        while len(chars) > idx:
            chars.pop()
        return idx + 1


s = Solution()
print(s.compress(["a", "a", "b", "b", "c", "c", "c"]))
print(s.compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))
