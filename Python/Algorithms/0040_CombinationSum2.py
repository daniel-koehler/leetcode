class Solution:
    
    def backtrack(self, candidates: List[int], nums: List[int], target: int, result: List[int]):
        if target == 0:
            tmp = sorted(copy.copy(nums))
            if tmp not in result:
                result.append(tmp)
            return
        
        if target < 0:
            return
        
        for i, cand in enumerate(candidates):
            nums.append(cand)
            self.backtrack(candidates[i+1:], nums, target-cand, result)
            del nums[-1]
        
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        for i, cand in enumerate(candidates):
            self.backtrack(candidates[i+1:], [cand], target-cand, result)
        return result