class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: list[int], informTime: list[int]) -> int:
        subordinates = [[] for _ in range(n)]
        total_time = [0] * n
        for (employee, man) in enumerate(manager):
            if man != -1:
                subordinates[man].append(employee)

        def dfs(emp, t):
            total_time[emp] = t
            for sub in subordinates[emp]:
                dfs(sub, t + informTime[emp])

        dfs(headID, 0)
        return max(total_time)


s = Solution()
print(s.numOfMinutes(1, 0, [-1], [0]))
print(s.numOfMinutes(6, 2, [2, 2, -1, 2, 2, 2], [0, 0, 1, 0, 0, 0]))
