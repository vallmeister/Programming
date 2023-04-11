class Solution:
    def maximalNetworkRank(self, n: int, roads: list[list[int]]) -> int:
        ranks = [0] * n
        for u, v in roads:
            ranks[u] += 1
            ranks[v] += 1
        roads = {(u, v) for (u, v) in roads}
        ranks = list(enumerate(ranks))
        ranks.sort(key=lambda x: x[1], reverse=True)
        max_rank = 0
        for i in range(n):
            for j in range(i):
                pair_rank = ranks[i][1] + ranks[j][1]
                if (ranks[i][0], ranks[j][0]) in roads or (ranks[j][0], ranks[i][0]) in roads:
                    pair_rank -= 1
                if max_rank < pair_rank:
                    max_rank = pair_rank
                elif max_rank > pair_rank:
                    break
        return max_rank


s = Solution()
print(s.maximalNetworkRank(4, [[0, 1], [0, 3], [1, 2], [1, 3]]))  # 4
print(s.maximalNetworkRank(5, [[0, 1], [0, 3], [1, 2], [1, 3], [2, 3], [2, 4]]))  # 5
print(s.maximalNetworkRank(8, [[0, 1], [1, 2], [2, 3], [2, 4], [5, 6], [5, 7]]))  # 5
