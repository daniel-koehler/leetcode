# Hashing rows and cols
# Time:  O(m*n)
# Space: O(m+n)
# Straight-forward approach saving rows and cols to be set to zero in dicts
class Solution:

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """ 
        rows = {}
        cols = {}
        m, n = len(matrix), len(matrix[0])
        i = 0
        while i < m:
            j = 0
            while j < n:
                if matrix[i][j] == 0:
                    rows[i] = None
                    cols[j] = None
                j += 1
            i += 1
            
        for i in range(m):
            for j in range(n):
                if i in rows or j in cols:
                    matrix[i][j] = 0

# Storing rows and cols
# Time:  O(m*n)
# Space: O(m+n)
# Straight-forward approach saving rows and cols to be set to zero in lists
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        rows = [0] * m
        cols = [0] * n        
        i = 0
        while i < m:
            j = 0
            while j < n:
                if matrix[i][j] == 0:
                    rows[i] = 1
                    cols[j] = 1
                j += 1
            i += 1
            
        for i in range(m):
            for j in range(n):
                if rows[i] or cols[j]:
                    matrix[i][j] = 0


# Alternative approach: use elements in the first row/col as indicators for constant space complexity