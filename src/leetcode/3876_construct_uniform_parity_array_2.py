class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n = len(nums1)
        min_odd_left = [10 ** 9] * n
        min_even_left = [10 ** 9] * n
        min_odd_right = [10 ** 9] * n
        min_even_right = [10 ** 9] * n
        for i in range(1, n):
            num = nums1[i - 1]
            if num % 2 == 0:
                min_even_left[i] = min(num, min_even_left[i - 1])
                min_odd_left[i] = min_odd_left[i - 1]
            else:
                min_even_left[i] = min_even_left[i - 1]
                min_odd_left[i] = min(min_odd_left[i - 1], num)
        for i in reversed(range(n - 1)):
            num = nums1[i + 1]
            if num % 2 == 0:
                min_odd_right[i] = min_odd_right[i + 1]
                min_even_right[i] = min(num, min_even_right[i + 1])
            else:
                min_odd_right[i] = min(min_odd_right[i + 1], num)
                min_even_right[i] = min_even_right[i + 1]

        # all even:
        for i in range(n):
            num = nums1[i]
            if num % 2 == 0:
                continue
            elif min_odd_left[i] >= num and min_odd_right[i] >= num:
                break
        else:
            return True

        # all odd
        for i in range(n):
            num = nums1[i]
            if num % 2 == 1:
                continue
            elif min_odd_left[i] >= num and min_odd_right[i] >= num:
                break
        else:
            return True

        return False


s = Solution()
print(s.uniformArray(nums1=[2, 3]))
