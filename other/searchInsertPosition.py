class searchInsertPosition:

    def solution(nums, target):
        length = len(nums)
        if length == 1:
            if target > nums[0]: return 1
            else: return 0
        elif target > nums[-1]: return length
        elif target < nums[0]: return 0

        lower = 0
        upper = length - 1

        while(lower < upper):
            current = (lower + upper) // 2
            if nums[current] == target: return current
            elif nums[current] < target: lower = current + 1
            elif nums[current] > target: upper = current - 1
        if nums[lower] < target: return lower + 1
        else: return lower

    nums = [1,3,5,6]
    target = 5
    print(solution(nums, target))

    target = 2
    print(solution(nums, target))

    target = 7
    print(solution(nums, target))

    target = 0
    nums = [1]
    print(solution(nums, target))

    nums = [1,3]
    target = 2
    print(solution(nums, target))
    