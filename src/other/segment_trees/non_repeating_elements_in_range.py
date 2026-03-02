import bisect
import math
from collections import defaultdict

segment_tree = []
occurrences = []
indices_of = defaultdict(list)


def preprocess(nums):
    for i, num in enumerate(nums):
        indices_of[num].append(i)
    for i, num in enumerate(nums):
        occurrences.append([0, 0])
        indices = [-math.inf] + indices_of[num] + [math.inf]
        j = bisect.bisect_left(indices, i)
        occurrences[i][0] = indices[j - 1]
        occurrences[i][1] = indices[j + 1]


def build(i, start, end):
    if start == end:
        segment_tree[i].append(occurrences[start])
    else:
        mid = (start + end) // 2
        build(2 * i, start, mid)
        build(2 * i + 1, mid + 1, end)


def build_tree(nums):
    global segment_tree
    n = len(nums)
    segment_tree = [[] for _ in range(4 * n)]
    build(1, 0, len(nums) - 1)


if __name__ == "__main__":
    arr = [1, 2, 1, 2, 3, 4]
    preprocess(arr)
    build_tree(arr)
