class Solution:
    def anagramMappings(self, nums1: list[int], nums2: list[int]) -> list[int]:
        n = len(nums1)
        mapping = [0] * n
        for i in range(n):
            for j in range(n):
                if nums2[j] == nums1[i]:
                    mapping[i] = j
                    nums2[j] = -1
                    break
        return mapping


s = Solution()
print(s.anagramMappings([12, 28, 46, 32, 50], [50, 12, 32, 46, 28]))
print(s.anagramMappings([84, 46], [84, 46]))
