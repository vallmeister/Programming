from collections import Counter
from heapq import heappush, heappop, heapify


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        heap = [(-ord(letter), count) for letter, count in Counter(s).items()]
        heapify(heap)
        ans = []
        while heap:
            idx, count = heappop(heap)
            letter = chr(-idx)
            if ans and letter == ans[-1]:
                if not heap:
                    break
                next_idx, next_count = heappop(heap)
                next_letter = chr(-next_idx)
                ans.append(next_letter)
                if next_count > 1:
                    heappush(heap, (next_idx, next_count - 1))
            else:
                repeat = min(count, repeatLimit)
                ans.extend([letter] * repeat)
                count -= repeat
            if count > 0:
                heappush(heap, (idx, count))
        return ''.join(ans)


sol = Solution()
print(sol.repeatLimitedString("cczazcc", 3))
print(sol.repeatLimitedString("aababab", 2))
print(sol.repeatLimitedString("xyutfpopdynbadwtvmxiemmusevduloxwvpkjioizvanetecnuqbqqdtrwrkgt", 1))
