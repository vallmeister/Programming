class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        q = [[0] * 4]
        deadends = set(deadends)
        if '0000' in deadends and '0000' != target:
            return -1
        deadends.add('0000')
        turns = 0
        while q:
            nq = []
            for combination in q:
                if ''.join([str(i) for i in combination]) == target:
                    return turns
                for i in range(4):
                    new_combination = combination[:i] + [(combination[i] + 1) % 10] + combination[i + 1:]
                    word = ''.join(str(i) for i in new_combination)
                    if word not in deadends:
                        nq.append(new_combination)
                        deadends.add(word)
                    new_combination = combination[:i] + [(combination[i] - 1) % 10] + combination[i + 1:]
                    word = ''.join(str(i) for i in new_combination)
                    if word not in deadends:
                        nq.append(new_combination)
                        deadends.add(word)
            turns += 1
            q = nq
        return -1


s = Solution()
print(s.openLock(["0201", "0101", "0102", "1212", "2002"], '0202'))
print(s.openLock(["8888"], '0009'))
print(s.openLock(['0000'], '8888'))
