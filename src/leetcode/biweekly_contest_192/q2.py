class Solution:
    def canTransform(self, source: list[int], target: list[int]) -> bool:
        n = len(source)
        for i in range(n - 1):
            if source[i] == target[i]:
                continue
            delta = source[i] + source[i + 1] - target[i]
            source[i + 1] = delta
        return source[-1] == target[-1]


s = Solution()
print(s.canTransform(source=[1, 2, 3], target=[0, 2, 4]))
print(s.canTransform(source=[-5, -5], target=[-15, 5]))
print(s.canTransform(source=[1, 2, 1], target=[0, 2, 5]))
print(s.canTransform([-77, -42], [72, 47]))
