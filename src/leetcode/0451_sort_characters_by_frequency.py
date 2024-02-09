from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        k = max(counter.values())
        buckets = [[] for _ in range(k + 1)]
        for letter, count in counter.items():
            buckets[count].append(letter)
        string_builder = []
        for i in reversed(range(k + 1)):
            for letter in buckets[i]:
                string_builder += [letter] * i
        return ''.join(string_builder)


sol = Solution()
print(sol.frequencySort('tree'))
