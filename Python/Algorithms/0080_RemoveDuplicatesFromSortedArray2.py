class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if len(nums) <= 1:
            return
        cnt = 0
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                cnt += 1
            else:
                cnt = 0
            
            if cnt > 1:
                del nums[i]
            else:
                i += 1