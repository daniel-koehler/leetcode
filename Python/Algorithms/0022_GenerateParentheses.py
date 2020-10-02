class Solution:
    
    def backtracking(self, n:int, combinations: Dict[str, int]=None) -> Dict[str, int]:
        if n == 0:
            return combinations
        elif not combinations:
            return self.backtracking(n-1, {'(': 1})
        else:
            new_combs = {}
            for comb, open_brackets in combinations.items():
                if comb[-1] == '(': 
                    new_combs[comb + ')'] = open_brackets - 1
                if comb[-1] == '(' and open_brackets < n:
                    new_combs[comb + '('] = open_brackets + 1    
                if comb[-1] == ')' and open_brackets < n:
                    new_combs[comb + '('] = open_brackets + 1
                if comb[-1] == ')' and open_brackets > 0:
                    new_combs[comb + ')'] = open_brackets - 1           
            return self.backtracking(n-1, new_combs)
                
    def generateParenthesis(self, n: int) -> List[str]:
        return self.backtracking(2*n)
        