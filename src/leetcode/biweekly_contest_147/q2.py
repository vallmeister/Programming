from heapq import heappush, heappop
from typing import List


class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.heap = []
        self.priorities = {}
        self.task_to_user = {}
        self.removed_tasks = set()
        for uid, tid, priority in tasks:
            self.add(uid, tid, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        heappush(self.heap, (-priority, -taskId, userId))
        self.priorities[taskId] = priority
        self.task_to_user[taskId] = userId
        if taskId in self.removed_tasks:
            self.removed_tasks.remove(taskId)

    def edit(self, taskId: int, newPriority: int) -> None:
        self.priorities[taskId] = newPriority
        user = self.task_to_user[taskId]
        heappush(self.heap, (-newPriority, -taskId, user))

    def rmv(self, taskId: int) -> None:
        self.removed_tasks.add(taskId)
        del self.priorities[taskId]
        del self.task_to_user[taskId]

    def execTop(self) -> int:
        while self.heap:
            priority, tid, user = heappop(self.heap)
            tid = -tid
            priority = -priority
            if tid in self.removed_tasks or priority != self.priorities[tid]:
                continue
            self.removed_tasks.add(tid)
            return user
        return -1

tm = TaskManager([[10,25,31]])
tm.edit(25, 9)
print(tm.execTop())

tm = TaskManager([[2,12,32],[3,27,33],[10,5,23],[8,4,3]])
tm.edit(4, 48)
print(tm.execTop())

tm = TaskManager([[3,12,4]])
tm.edit(12, 27)
tm.edit(12, 33)
print(tm.execTop())
print(tm.execTop())
print(tm.execTop())
