import math



# TODO: make it work
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        if len(n) == 1:
            return str(int(n) - 1)
        candidates = ["9" * (len(n) - 1), "1" + "0" * (len(n) - 1) + "1"]

        digits = list(n)
        
        def backtracking(i, j):
            if i > j:
                candidates.append("".join(digits))
                return
            elif i == j:
                backtracking(i + 1, j - 1)
                tmp = digits[i]
                new = int(tmp) - 1 + 10
                new %= 10
                digits[i] = str(new)
                backtracking(i + 1, j - 1)
                new = int(tmp) + 1
                new %= 10
                digits[i] = str(new)
                backtracking(i + 1, j - 1)
                digits[i] = tmp
                return
            elif j - i == 1 and digits[i] == digits[j]:
                tmp = digits[i]
                new = int(tmp) - 1 + 10
                new %= 10
                digits[i] = str(new)
                digits[j] = str(new)
                backtracking(i + 1, j - 1)
                new = int(tmp) + 1
                new %= 10
                digits[i] = str(new)
                digits[j] = str(new)
                backtracking(i + 1, j - 1)
                digits[i] = tmp
                digits[j] = tmp
                return
            fst = digits[i]
            lst = digits[j]
            if digits[i] == digits[j]:
                return backtracking(i + 1, j - 1)
            else:
                digits[j] = digits[i]
                backtracking(i + 1, j - 1)
                digits[j] = lst
                digits[i] = digits[j]
                backtracking(i + 1, j - 1)
                digits[i] = fst
        
        backtracking(0, len(n) - 1)
        min_diff = math.inf
        curr = math.inf
        print(candidates)
        for candidate in candidates:
            if candidate == n or candidate.startswith("0"):
                continue
            diff = abs(int(n) - int(candidate))
            if diff < min_diff:
                min_diff = diff
                curr = int(candidate)
            elif diff == min_diff:
                curr = min(int(candidate), curr)
        return str(curr)


s = Solution()
print(s.nearestPalindromic("1283"))
