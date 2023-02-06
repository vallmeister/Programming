# Intuitive approach, needs O(n) extra space
def shuffle_easy(nums: list[int], n: int) -> list[int]:
    result = []
    xs = nums[:n]
    ys = nums[n:]
    for i in range(n):
        result.append(xs[i])
        result.append(ys[i])
    return result


print(shuffle_easy([2, 5, 1, 3, 4, 7], 3))
print(shuffle_easy([1, 2, 3, 4, 4, 3, 2, 1], 4))
print(shuffle_easy([1, 1, 2, 2], 2))
