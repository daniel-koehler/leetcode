# Linear search
# Time:  O(n)
# Space: O(1)
class Solution1:
    def search(self, nums: List[int], target: int) -> int:
        
        for i, n in enumerate(nums):
            if n == target:
                return i
        return -1

# Linear search with index()
# Time:  O(n)
# Space: O(1)
class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            return -1

#TODO(daniel): binary search