from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        inc = '++'
        dec = '--'
        for op in operations:
            if op.startswith(inc) or op.endswith(inc):
                x += 1
            elif op.startswith(dec) or op.endswith(dec):
                x -= 1
        return x
