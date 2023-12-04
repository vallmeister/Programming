from collections import Counter, defaultdict
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ans = []
        size = len(words[0])
        m = len(s)
        n = len(words)

        def sliding_window(left):
            curr_window = defaultdict(int)
            words_count = Counter(words)
            count = 0
            while left < m:
                right = left
                while right + size <= m and s[right:right + size] in words_count:
                    next_word = s[right:right + size]
                    curr_window[next_word] += 1
                    count += 1
                    while curr_window[next_word] > words_count[next_word]:
                        first_word = s[left:left + size]
                        curr_window[first_word] -= 1
                        count -= 1
                        left += size
                    if count == n:
                        ans.append(left)
                    right += size
                else:
                    left = right + 1
                    count = 0
                    curr_window = defaultdict(int)

        for i in range(size):
            sliding_window(i)
        return ans


sol = Solution()
print(sol.findSubstring("barfoothefoobarman", words=["foo", "bar"]))
print(sol.findSubstring("wordgoodgoodgoodbestword", words=["word", "good", "best", "word"]))
print(sol.findSubstring("barfoofoobarthefoobarman", words=["bar", "foo", "the"]))
print(sol.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "good"]))
print(sol.findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo", "barr", "wing", "ding", "wing"]))
print(sol.findSubstring("aaaaaaaaaaaaaa", ["aa", "aa"]))  # TODO: fix this
