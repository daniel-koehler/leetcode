# 2D Binary search
# Time:  O(log(n) + log(m))
# Space: O(1)
# First try to find a row that covers an interval including the target
# and then search within the row.
class Solution:
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        try:
            m, n = len(matrix), len(matrix[0])
        except IndexError:
            return False
        
        if n == 0:
            return False
        
        l, r = 0, m - 1
        
        while l <= r:
            m0 = (l + r) // 2
            if matrix[m0][0] <= target and matrix[m0][-1] >= target:
                break
            elif matrix[m0][0] < target:
                l = m0 + 1
            else:
                r = m0 - 1
        else:
            return False
        
        l, r = 0, n - 1
        
        while l <= r:
            n0 = (l + r) // 2
            if matrix[m0][n0] == target:
                return True
            elif matrix[m0][n0] < target:
                l = n0 + 1
            else:
                r = n0 - 1

        return False

# Linearized binary search
# Time:  O(log(n+m))
# Space: O(1)
# Try to find the target with a single binary search
class Solution:
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        try:
            m, n = len(matrix), len(matrix[0])
        except IndexError:
            return False
        
        l, r = 0, (n * m) - 1
        
        while l <= r:
            mid = (l + r) // 2
            row, col = divmod(mid, n)
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False