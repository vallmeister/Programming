from collections import deque
from typing import List


class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        ans = [0] * numberOfUsers
        online = [True] * numberOfUsers
        offline_q = deque()
        events.sort(key=lambda event: (int(event[1]), 1 if event[0] == "MESSAGE" else 0))
        all_count = 0
        for event_type, timestamp, message in events:
            timestamp = int(timestamp)
            while offline_q and offline_q[0][0] <= int(timestamp):
                _, user = offline_q.popleft()
                online[user] = True
            match event_type:
                case "MESSAGE":
                    match message:
                        case "ALL":
                            all_count += 1
                        case "HERE":
                            for i in range(numberOfUsers):
                                if online[i]:
                                    ans[i] += 1
                        case _:
                            for idx in message.split():
                                user = int(idx[2:])
                                ans[user] += 1
                case "OFFLINE":
                    user = int(message)
                    offline_q.append((timestamp + 60, user))
                    online[user] = False
        for i in range(numberOfUsers):
            ans[i] += all_count
        return ans


s = Solution()
print(s.countMentions(numberOfUsers=2,
                      events=[["MESSAGE", "10", "id1 id0"], ["OFFLINE", "11", "0"], ["MESSAGE", "71", "HERE"]]))
print(s.countMentions(numberOfUsers=2,
                      events=[["MESSAGE", "10", "id1 id0"], ["OFFLINE", "11", "0"], ["MESSAGE", "12", "ALL"]]))
print(s.countMentions(numberOfUsers=2, events=[["OFFLINE", "10", "0"], ["MESSAGE", "12", "HERE"]]))
print(s.countMentions(3, [["MESSAGE", "2", "HERE"], ["OFFLINE", "2", "1"], ["OFFLINE", "1", "0"],
                          ["MESSAGE", "61", "HERE"]]))
