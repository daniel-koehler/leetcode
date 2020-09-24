# Brute force solution
# Time:  O(n^2)
# Space: O(1)
# Use nested loop
class SolutionBruteForce:
     def twoSum(self, nums: List[int], target: int) -> List[int]:
         for i, num1 in enumerate(nums):
             for j, num2 in enumerate(nums):
                 if num1 + num2 == target and i != j:
                     return [i, j]

# Enhanced brute force solution
# Time:  O(n^2)
# Space: O(1)
# Use nested loops, but compute the sum of each number pair only once
class SolutionBruteForceEnhanced:
     def twoSum(self, nums: List[int], target: int) -> List[int]:
         for i, num1 in enumerate(nums):
             for j in range(i+1, len(nums)):
                 if num1 + nums[j] == target:
                     return [i, j]

# Single pass with hash map
# Time:  O(n)
# Space: O(n)
# Iterate over the numbers and store each index:number pair in a hash map.
class SolutionHashMap:
     def twoSum(self, nums: List[int], target: int) -> List[int]:
         indices = {}
         for i, num in enumerate(nums):
             try:
                 return [i, indices[target - num]]
             except KeyError:
                 indices[num] = i