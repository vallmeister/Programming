class Solution:
    def numberOfWays(self, corridor: str) -> int:
        n = len(corridor)
        MOD = 10 ** 9 + 7
        dp = [[0] * 3 for _ in range(n + 1)]
        dp[n][2] = 1

        for i in reversed(range(n)):
            for seats in range(3):
                if seats < 2:
                    dp[i][seats] = dp[i + 1][seats + (1 if corridor[i] == 'S' else 0)]
                elif corridor[i] == 'S':
                    dp[i][seats] = dp[i + 1][1]
                else:
                    dp[i][seats] = dp[i + 1][0] + dp[i + 1][seats]
                dp[i][seats] %= MOD
        return dp[0][0] % MOD

        # def memo(i, seats):
        #     if i >= n:
        #         return (1 if seats == 2 else 0)
        #     elif dp[i][seats] != -1:
        #         return dp[i][seats]
        #     res = 0
        #     if seats < 2:
        #         res = memo(i + 1, seats + (1 if corridor[i] == 'S' else 0))
        #     elif corridor[i] == 'S':
        #         res = memo(i + 1, 1)
        #     else:
        #         res = (memo(i + 1, 0) + memo(i + 1, seats)) % MOD
        #     dp[i][seats] = res
        #     return res

        return memo(0, 0) % MOD


s = Solution()
print(s.numberOfWays("SSPPSPS"))
print(s.numberOfWays("PPSPSP"))
print(s.numberOfWays("S"))
print(s.numberOfWays("SS"))
print(s.numberOfWays("P"))
print(s.numberOfWays("SPPSSSSPPS"))
print(s.numberOfWays("SPSPPSSPSSSS"))
print(s.numberOfWays(
    "SPPPPPPPSPPPSPSSSPPPPPPPPPPPPPPPPPSPPPPPPPPPPPPPPPPSPPPPPSPSPPPPPPSPSPPSPSPPPSPSPPSSPPPPPSPPSSPP"))  # 0
