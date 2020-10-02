class Solution:

    def backtrack(self, candidates: List[int], target: int, nums: List[int]=None, result: List[int]=None):
        if target == 0:
            result.append(copy.copy(nums))
            return
        
        if target < 0:
            return
        
        for i, cand in enumerate(candidates):
            nums.append(cand)
            self.backtrack(candidates[i:], target-cand, nums, result)
            del nums[-1]
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        for i, cand in enumerate(candidates):
            self.backtrack(candidates[i:], target-cand, [cand], result=result)
            
        return result