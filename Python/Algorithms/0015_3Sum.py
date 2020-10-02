# Two pointer approach
class Solution:
    from collections import defaultdict
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        summands = []
        if l < 3:
            return summands
        
        nums.sort()
        i, prev = 0, None
        while i < l - 2: 
            if nums[i] != prev:
                compl = - nums[i]
                low, high = i+1, l-1
                prev = nums[i]
                while low < high:
                    _sum = nums[low] + nums[high]
                    if _sum == compl:
                        summands.append([nums[i], nums[low], nums[high]])

                        while (low < high) and (nums[low]==nums[low+1]):
                            low += 1
                        while (low < high) and (nums[high]==nums[high-1]):
                            high -= 1

                        low += 1
                        high -= 1
                    
                    elif _sum < compl:
                        low += 1
                    else:
                        high -= 1
            i += 1