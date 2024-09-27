class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        m = len(slots1)
        n = len(slots2)
        i = j = 0
        while i < m and j < n:
            s1, e1 = slots1[i]
            s2, e2 = slots2[j]
            if e1 - s1 < duration or e1 < s2:
                i += 1
            elif e2 - s2 < duration or e2 < s1:
                j += 1
            elif min(e1, e2) - max(s1, s2) < duration:
                if s1 < s2:
                    i += 1
                elif s1 > s2:
                    j += 1
            else:
                return [max(s1, s2), max(s1, s2) + duration]
        return []
