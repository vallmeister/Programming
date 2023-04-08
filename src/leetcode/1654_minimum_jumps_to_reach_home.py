class Solution:
    def minimumJumps(self, forbidden: list[int], a: int, b: int, x: int) -> int:
        forbidden = set(forbidden)
        distance = 0
        upper_bound = max(x, max(forbidden)) + b + a
        q = [(0, True)]
        visited = {(0, True)}
        while q:
            nq = []
            for idx, can_jump_backward in q:
                if idx == x:
                    return distance
                backward = idx - b
                if can_jump_backward and backward >= 0 and backward not in forbidden and (
                        backward, False) not in visited:
                    visited.add((backward, False))
                    nq.append((backward, False))
                forward = idx + a
                if forward <= upper_bound and forward not in forbidden and (forward, True) not in visited:
                    visited.add((forward, True))
                    nq.append((forward, True))
            q = nq
            distance += 1
        return -1


s = Solution()
print(s.minimumJumps([14, 4, 18, 1, 15], 3, 15, 9))
print(s.minimumJumps([8, 3, 16, 6, 12, 20], 15, 13, 11))
print(s.minimumJumps([1, 6, 2, 14, 5, 17, 4], 16, 9, 7))
print(s.minimumJumps(
    [162, 118, 178, 152, 167, 100, 40, 74, 199, 186, 26, 73, 200, 127, 30, 124, 193, 84, 184, 36, 103, 149, 153, 9, 54,
     154, 133, 95, 45, 198, 79, 157, 64, 122, 59, 71, 48, 177, 82, 35, 14, 176, 16, 108, 111, 6, 168, 31, 134, 164, 136,
     72, 98], 29, 98, 80))
print(s.minimumJumps([1998], 1999, 2000, 2000))
