# Dynamic programming - Bottum-up
# Time:  O(n*m)
# Space: O(1)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # Trivial case (only one path)
        if m == 1 or n == 1:
            return sum([sum(row) for row in grid])
        
        # Calculate path costs in row 0 and col 0
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]   
        for i in range(1, n):
            grid[0][i] += grid[0][i-1]
            
        # Calculate path costs for the remaining fields
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
                
        return grid[i][j]