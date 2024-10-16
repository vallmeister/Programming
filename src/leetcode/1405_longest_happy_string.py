from heapq import heappush, heappop


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a > 0:
            heappush(heap, (-a, 'a'))
        if b > 0:
            heappush(heap, (-b, 'b'))
        if c > 0:
            heappush(heap, (-c, 'c'))
        ans = []
        while heap:
            count, char = heappop(heap)
            count = -count
            if len(ans) >= 2 and ans[-1] == char and ans[-2] == char:
                if not heap:
                    break
                tmp_count, tmp_char = heappop(heap)
                ans.append(tmp_char)
                if -tmp_count > 1:
                    heappush(heap, (tmp_count + 1, tmp_char))
                heappush(heap, (-count, char))
            else:
                count -= 1
                ans.append(char)
                if count > 0:
                    heappush(heap, (-count, char))
        return ''.join(ans)
