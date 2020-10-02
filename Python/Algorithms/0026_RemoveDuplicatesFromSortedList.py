# Time:  O(n)
# Space: O(1)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        while (i < len(nums)):
            if nums[i] == nums[i-1]:
                prev = nums[i]
                del nums[i]
            else:
                prev = nums[i]
                i += 1
        return i