# Solution with backtracking
class Solution:
    
    def backtrack(self, nums: List[int], comb: List[int], result: List[int]):
        if not nums:
            result.append(copy.copy(comb))
            return
        
        for i, num in enumerate(nums):
            comb.append(num)
            n = list(nums)
            del n[i]
            self.backtrack(n, comb, result)
            del comb[-1]  
                
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i, cand in enumerate(nums):
            n = list(nums)
            del n[i]
            self.backtrack(n, [cand], result)
        return result

# Solution with recursive generator
class Solution:

    def permutations(self, nums: List[int]):
        if not nums:
            yield []
        for num in nums:
            remaining = list(nums)
            remaining.remove(num)
            for perm in self.permutations(remaining):
                yield [num] + list(perm)
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(self.permutations(nums))
