class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if start.replace('_', '') != target.replace('_', ''):
            return False
        n = len(start)
        i = j = 0
        while i < n and j < n:
            while j < n and target[j] != 'L':
                j += 1
            while i < n and start[i] != 'L':
                i += 1
            if j > i:
                return False
            i += 1
            j += 1

        i = j = n - 1
        while i >= 0 and j >= 0:
            while j >= 0 and target[j] != 'R':
                j -= 1
            while i >= 0 and start[i] != 'R':
                i -= 1
            if j < i:
                return False
            i -= 1
            j -= 1
        return True
