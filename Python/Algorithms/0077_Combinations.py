# Using a recursive generator
class SolutionGenerator:
    
    def permutations(self, nums: List[int], length: int):
        if length == 0:
            yield []
        for i in range(len(nums)):
            for perm in self.permutations(nums[i+1:], length-1):
                yield [nums[i]] + list(perm)
                
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(self.permutations([i for i in range(1, n+1)], k))