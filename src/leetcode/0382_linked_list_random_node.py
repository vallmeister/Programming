# Definition for singly-linked list.
import random
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.hd = head

    def getRandom(self) -> int:
        n = 0
        tmp = self.hd
        memo = {n: tmp}
        while tmp.next is not None:
            n += 1
            tmp = tmp.next
            memo[n] = tmp
        rn = random.randint(0, n)
        return memo[rn].val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
