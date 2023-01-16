def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    if not intervals:
        return [newInterval]
    if intervals[-1][0] <= newInterval[0]:
        if intervals[-1][1] >= newInterval[0]:
            intervals[-1][0] = min(intervals[-1][0], newInterval[0])
            intervals[-1][1] = max(intervals[-1][1], newInterval[1])
        else:
            intervals.append(newInterval)
        return intervals
    
    for (idx, interval) in enumerate(intervals):
        if interval[0] > newInterval[0]:
            intervals.insert(idx, newInterval)
            break
    idx = 1
    while idx < len(intervals):
        if intervals[idx - 1][1] >= intervals[idx][0]:
            intervals[idx - 1][1] = max(intervals[idx - 1][1], intervals[idx][1])
            del intervals[idx]
            continue
        idx += 1
    return intervals


print(insert([[1, 3], [6, 9]], [2, 5]))
print(insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
