from collections import defaultdict, deque


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        bank_dict = defaultdict(set)
        bank = set(bank)

        def generate_mutations(gene):
            mutations = set()
            for i in range(len(gene)):
                mutation = gene[:i] + '*' + gene[i + 1:]
                mutations.add(mutation)
            return mutations

        for valid_gene in bank:
            valid_mutations = generate_mutations(valid_gene)
            for vm in valid_mutations:
                bank_dict[vm].add(valid_gene)

        q = deque()
        q.append((startGene, 0))
        visited = set()
        while q:
            gene, num_mutations = q.popleft()
            if gene in visited:
                continue
            elif gene == endGene:
                return num_mutations
            visited.add(gene)
            mutations = generate_mutations(gene)
            for mutation in mutations:
                for valid_mutation in bank_dict[mutation]:
                    q.append((valid_mutation, num_mutations + 1))

        return -1


s = Solution()
print(s.minMutation('AACCGGTT', 'AACCGGTA', ["AACCGGTA"]))
print(s.minMutation('AACCGGTT', 'AAACGGTA', ["AACCGGTA", "AACCGCTA", "AAACGGTA"]))
