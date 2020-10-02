# Two pointers
# Time:  O(n^2)
# Space: O(n) for sorting
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        l = len(nums)
        nums.sort()
        prev = None
        smallest_diff = 2**31 - 1
        i = 0
        for i in range(l-2):
            if nums[i] == prev:
                continue
            low, high = i+1, l-1
            prev = nums[i]
            while (low < high):
                _sum = nums[i] + nums[low] + nums[high]
                diff = abs(_sum - target)
                if diff < smallest_diff:
                    smallest_diff = diff
                    closest_sum = _sum
                
                if _sum < target:
                    low += 1
                else:
                    high -= 1
            
        return closest_sum

# Binary search
# Time:  O(n^2 log(n))
# Space: O(n) for sorting
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:  
        l = len(nums)
        nums.sort()
        smallest_diff = 2**31-1
        
        for i in range(l):
            for j in range(i+1, l):
                complement = target - nums[i] - nums[j]
                low, high = j+1, l-1

                while low <= high:
                    mid = (low + high) // 2
                    diff = abs(complement - nums[mid])
                    
                    if diff < smallest_diff:
                        smallest_diff = diff
                        closest_sum = nums[i] + nums[j] + nums[mid]

                    if diff == 0:
                        break
                        
                    if complement > nums[mid]:
                        low = mid + 1
                    else:
                        high = mid - 1
        
        return closest_sum