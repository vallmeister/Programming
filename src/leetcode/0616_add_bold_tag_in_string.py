class Solution:
    # TODO: Revisit this exercise
    def addBoldTag(self, s: str, words: list[str]) -> str:
        if not words:
            return s
        intervals = []
        words = set(words)
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in words:
                    intervals.append([i, j - 1])
        if not intervals:
            return s
        # merge intervals; note that intervals are already sorted by construction
        merged_intervals = []
        curr_interval = intervals[0]
        for interval in intervals[1:]:
            if curr_interval[1] + 1 >= interval[0]:  # merge
                curr_interval[1] = max(interval[1], curr_interval[1])
            else:
                merged_intervals.append(curr_interval)
                curr_interval = interval
        merged_intervals.append(curr_interval)
        tagged_string = []
        i = 0
        for start, end in merged_intervals:
            while i < start:
                tagged_string.append(s[i])
                i += 1
            tagged_string.append('<b>')
            while start <= i <= end:
                tagged_string.append(s[i])
                i += 1
            tagged_string.append('</b>')
        while i < len(s):
            tagged_string.append(s[i])
            i += 1
        return ''.join(tagged_string)


sol = Solution()
print(sol.addBoldTag("abcxyz123", words=["abc", "123"]))
print(sol.addBoldTag("aaabbb", words=["aa", "b"]))
print(sol.addBoldTag("aaabbcc", ["aaa", "aab", "bc"]))
print(sol.addBoldTag("aaabbcc", ["aaa", "aab", "bc", "aaabbcc"]))
print(sol.addBoldTag("aaabbcc", []))
print(sol.addBoldTag("aaabbcc", ['d']))
