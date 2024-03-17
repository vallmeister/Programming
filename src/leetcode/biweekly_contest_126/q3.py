from heapq import heapify, heappop, heappush


class Solution:
    def minimizeStringValue(self, s: str) -> str:
        freq = {char: 0 for char in 'abcdefghijklmnopqrstuvwxyz'}
        for char in s:
            if char != '?':
                freq[char] += 1
        heap = [(v, k) for k, v in freq.items()]
        heapify(heap)
        s = list(s)
        replacements = []
        for i, char in enumerate(s):
            if char == '?':
                f, nc = heap[0]
                while freq[nc] != f:
                    heappop(heap)
                    heappush(heap, (freq[nc], nc))
                    f, nc = heap[0]
                _, nc = heappop(heap)
                replacements.append(nc)
                freq[nc] += 1
                heappush(heap, (freq[nc], nc))
        replacements.sort(reverse=True)
        for i, char in enumerate(s):
            if char == '?':
                s[i] = replacements.pop()
        return ''.join(s)


sol = Solution()
print(sol.minimizeStringValue('???'))
print(sol.minimizeStringValue('a?a?'))
print(sol.minimizeStringValue("abcdefghijklmnopqrstuvwxy??"))
print(sol.minimizeStringValue("??s?c?gsihjd?o?xd"))
print(sol.minimizeStringValue("eq?umjlasi"))
