class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        bank = set(bank)
        if endGene not in bank:
            return -1
        mutations = 0
        q = [startGene]
        while q:
            nq = []
            for gene in q:
                if gene == endGene:
                    return mutations
                visited = set()
                for mutation in bank:
                    if self.edit_distance(gene, mutation) == 1:
                        nq.append(mutation)
                        visited.add(mutation)
                bank -= visited
            mutations += 1
            q = nq
        return -1

    def edit_distance(self, s1, s2):
        distance = 0
        for i in range(8):
            if s1[i] != s2[i]:
                distance += 1
        return distance


s = Solution()
print(s.minMutation('AACCGGTT', 'AACCGGTA', ["AACCGGTA"]))
print(s.minMutation('AACCGGTT', 'AAACGGTA', ["AACCGGTA", "AACCGCTA", "AAACGGTA"]))
