from typing import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        longest = 0
        arr1 = [str(num) for num in arr1]
        arr2 = [str(num) for num in arr2]
        if len(arr1) < len(arr2):
            arr1, arr2 = arr2, arr1

        trie = {}
        for num in arr1:
            curr = trie
            for digit in num:
                if digit not in curr:
                    curr[digit] = {}
                curr = curr[digit]
            curr['*'] = num

        for num in arr2:
            curr_node = trie
            curr_pref = 0
            while curr_pref < len(num) and num[curr_pref] in curr_node:
                curr_node = curr_node[num[curr_pref]]
                curr_pref += 1
            longest = max(longest, curr_pref)

        return longest
