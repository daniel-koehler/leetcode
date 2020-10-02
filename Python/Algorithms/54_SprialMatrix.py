# Time:  O(n*m), for an n x m matrix
# Space: O(1)
class Solution:
    
    def changeDir(self, direction: List[int]):
        direction[0], direction[1] = direction[1], -direction[0]
    
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        _dir = [0, 1]
        l = len(matrix) * len(matrix[0])
        b0, bx, by = 0, len(matrix)-1, len(matrix[0])-1
        i, j, k = 0, 0, 0
        res = []
        while l > 0:
            if _dir == [-1, 0] and i == b0+1:
                b0 += 1
                bx -= 1
                by -= 1
                self.changeDir(_dir)
            elif _dir == [0, 1] and j == by:
                self.changeDir(_dir)
            elif _dir == [1, 0] and i == bx:
                self.changeDir(_dir)
            elif _dir == [0, -1] and j == b0:
                self.changeDir(_dir)
            
            res.append(matrix[i][j])
            i += _dir[0]
            j += _dir[1]
            l -= 1
        return res