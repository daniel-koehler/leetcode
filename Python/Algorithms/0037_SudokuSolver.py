class Solution:
    
    def __init__(self):  
        self.size = 9
        self.sudoku_nums = [str(i) for i in range(1, self.size+1)]
        
        # Store the values present in each row/column/cell
        self.rows = {i: set() for i in range(self.size)}
        self.cols = {i: set() for i in range(self.size)}
        self.cells = {i: set() for i in range(self.size)}
        
    def cell_idx(self, row: int, col: int) -> int:
        return 3 * (row // 3) + col // 3
    
    def backtrack(self, board: List[List[str]], field: int) -> bool:
        # all fields are filled
        if field == self.size**2:
            return True
        
        row, col = divmod(field, self.size)

        # current field is already filled, check next
        if board[row][col] != '.':
            return self.backtrack(board, field+1)

        # check all possible candidates for the current field
        for value in self.sudoku_nums:
            if (value in self.rows[row]) or (value in self.cols[col]) or (value in self.cells[self.cell_idx(row, col)]):
                continue
                
            # value is possible candidate
            board[row][col] = value
            self.rows[row].add(value)
            self.cols[col].add(value)
            self.cells[self.cell_idx(row, col)].add(value)

            # candidate is valid
            if self.backtrack(board, field+1):
                return True

            #candidate is invalid, try next one
            board[row][col] = '.'
            self.rows[row].remove(value)
            self.cols[col].remove(value)
            self.cells[self.cell_idx(row, col)].remove(value)
                
        # no possible candidates -> invalid sudoku
        return False
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # initialize the hashmaps
        for row in range(self.size):
            for col in range(self.size):
                value = board[row][col]
                if value != '.':
                    self.rows[row].add(value)
                    self.cols[col].add(value)
                    self.cells[self.cell_idx(row, col)].add(value)
        
        # start backtracking at the first field
        self.backtrack(board, 0)
        return board 