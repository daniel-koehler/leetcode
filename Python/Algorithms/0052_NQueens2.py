class Solution:
    
    def setup(self, n):
        
        self.size = n
        
        # keep track of occupied rows / diagonals
        self.rows = [0] * n
        self.l2r_diag = {}
        self.r2l_diag = {}
        
        # calculate diagonal index
        self.l2r = lambda pos: pos[0] - pos[1]
        self.r2l = lambda pos: pos[0] - (self.size - pos[1] - 1)
        
        # stores the positions of placed queens
        self.queens = {}
        
        self.n_solutions = 0
    
        
    
    def isvalid(self, pos: List[int]) -> bool:
        
        if self.l2r(pos) in self.l2r_diag or self.r2l(pos) in self.r2l_diag:
            return False
        self.l2r_diag[self.l2r(pos)] = 0
        self.r2l_diag[self.r2l(pos)] = 0
        return True
    
    def backtrack(self, col: int=0):
        
        # found a solution
        if col == self.size:
            self.n_solutions += 1
            return
        
        # go row by row to check possible candidates
        for i in range(self.size):
            
            # there already is a queen in the current row
            if self.rows[i]:
                continue
            
            self.rows[i] = 1
            candidate = (i, col)
            
            
            if self.isvalid(candidate):
                # add queen to board and check next column
                self.queens[candidate] = None
                self.backtrack(col + 1)
                
                # remove the last queen
                del self.queens[candidate]
                del self.l2r_diag[self.l2r(candidate)]
                del self.r2l_diag[self.r2l(candidate)]
                
            self.rows[i] = 0
    
    def totalNQueens(self, n: int) -> int:
        self.setup(n)
        self.backtrack()
        return self.n_solutions