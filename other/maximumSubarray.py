class maximumSubarray:

    def solution(nums):
        best_sum = float('-inf')
        current_sum = 0

        for x in nums:
            current_sum = max(x, current_sum + x)
            best_sum = max(best_sum, current_sum)

        return best_sum

    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(solution(nums))

    nums = [1]
    print(solution(nums))

    nums = [5,4,-1,7,8]
    print(solution(nums))
    