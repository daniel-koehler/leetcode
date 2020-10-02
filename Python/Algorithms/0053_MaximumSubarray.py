# Kadane's algorithm
# Time:  O(n)
# Space: O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        max_sum = -2**31
        for i, num in enumerate(nums):
            curr_sum += num
            max_sum = max(max_sum, curr_sum)
            curr_sum = max(0, curr_sum)
        return max_sum