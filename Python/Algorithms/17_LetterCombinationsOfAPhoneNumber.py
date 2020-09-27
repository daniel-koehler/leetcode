# Backtracking
# Time:  O(3^n * 4^m) where n/ is the number of digits with 3/4 letter equivalents in the string
# Space: O(3^n * 4^m)
class Solution:
    
    def backtrack(self, digits: str, combinations: List[str]) -> List[str]:
        num_to_char = [
            None,
            None,
            ['a', 'b', 'c'],
            ['d', 'e', 'f'],
            ['g', 'h', 'i'],
            ['j', 'k', 'l'],
            ['m', 'n', 'o'],
            ['p', 'q', 'r', 's'],
            ['t', 'u', 'v'],
            ['w', 'x', 'y', 'z']
        ]
        if digits == '':
            return combinations
        return self.backtrack(digits[1:], [comb + letter for letter in num_to_char[int(digits[0])] for comb in combinations])
    
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
        return self.backtrack(digits, [''])