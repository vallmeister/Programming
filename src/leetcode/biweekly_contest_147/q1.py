class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        n = len(s)
        asterisk = p.find('*')
        left_pattern = p[:asterisk]
        right_pattern = p[asterisk + 1:]
        if not left_pattern:
            return self.find_substring(s, right_pattern)
        elif not right_pattern:
            return self.find_substring(s, left_pattern)
        for i in range(n):
            if self.find_substring(s[:i], left_pattern) and self.find_substring(s[i:], right_pattern):
                return True
        return False

    def find_substring(self, s, substring):
        n = len(s)
        for i in range(n):
            for j in range(i, n + 1):
                if s[i:j] == substring:
                    return True
        return False


sol = Solution()
print(sol.hasMatch("ojjju", "*o"))
