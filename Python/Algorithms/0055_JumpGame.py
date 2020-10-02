# Backtracking
# Time:  O(2^n)
# Space: O(n)
class Solution:
    
    def canJumpFrom(self, nums: List[int], index: int) -> bool:
        
        if index == len(nums) - 1:
            return True
        
        distance = min(nums[index] + index, len(nums)-1)
        for next_pos in range(distance, index, -1):
            if self.canJumpFrom(nums, next_pos):
                return True
            
        return False
    
    def canJump(self, nums: List[int]) -> bool: 
        return self.canJumpFrom(nums, 0)

# Single-pass with memoization
class Solution:
    def canJump(self, nums: List[int]) -> bool:
            l = len(nums)
            reachable = [False] * l
            reachable[0] = True
            for i in range(l):
                if reachable[i]:
                    reachable[i:i+nums[i]+1] = [True] * (nums[i]+1)
            return reachable[i]

# Greedy search
# Time:  O(n)
# Space: O(1)
class Solution:	
		
	
		
	def canJump(self, nums: List[int]) -> bool:
        last_pos = len(nums) - 1
        for i in range(last_pos, -1, -1):
            if i + nums[i] >= last_pos:
                last_pos = i   
        return last_pos == 0


#TODO(daniel): dynamic programming