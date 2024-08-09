class Solution:
    # TODO: correct
    def numberOfPatterns(self, m: int, n: int) -> int:
        ans = 0

        def backtrack(row, col, visited):
            nonlocal ans
            visited.add((row, col))
            if m <= len(visited) <= n:
                ans += 1
            for next_row in range(3):
                for next_col in range(3):
                    if (next_row, next_col) in visited:
                        continue
                    elif row == next_row and any((row, tmp_col) not in visited for tmp_col in
                                                 range(min(col, next_col) + 1, max(col, next_col))):
                        continue
                    elif col == next_col and any((tmp_row, col) not in visited for tmp_row in
                                                 range(min(row, next_row) + 1, max(row, next_row))):
                        continue
                    elif row == col and next_row == next_col and any(
                            (k, k) not in visited for k in range(min(row, next_row) + 1, max(row, next_row))):
                        continue
                    backtrack(next_row, next_col, visited)
            visited.remove((row, col))

        for i in range(3):
            for j in range(3):
                backtrack(i, j, set())
        return ans


s = Solution()
print(s.numberOfPatterns(1, 1))
print(s.numberOfPatterns(1, 2))
