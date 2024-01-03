from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        last_row = 0
        for row in bank:
            curr_row = row.count('1')
            if curr_row == 0:
                continue
            ans += curr_row * last_row
            last_row = curr_row
        return ans


s = Solution()
print(s.numberOfBeams(["011001", "000000", "010100", "001000"]))
print(s.numberOfBeams(["000", "111", "000"]))
