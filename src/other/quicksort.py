def quicksort(arr):
    n = len(arr)
    if n in {0, 1}:
        return arr
    pivot = arr.pop()
    left = []
    right = []
    for num in arr:
        if num <= pivot:
            left.append(num)
        else:
            right.append(num)
    return quicksort(left) + [pivot] + quicksort(right)


print(quicksort([1, 4, 5, 1, 3, 4]))
print(quicksort(
    [5, 19, 29, 1, 24, 22, 28, 14, 8, 21, 23, 11, 6, 30, 25, 16, 10, 2, 9, 20, 7, 15, 17, 26, 27, 18, 4, 3, 12, 13]))
