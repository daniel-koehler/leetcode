class Solution:
    
    def changeDir(self, direction: List[int]):
        direction[0], direction[1] = direction[1], -direction[0]
    
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        if n == 0: 
            return []
        bounds = [0, n-1]
        A = [[0 for i in range(n)] for j in range(n)]
        _dir = [0, 1]
        i, j = 0, 0
        for a in range(1,n*n+1):
            A[i][j] = a     
            if _dir == [-1, 0] and i == bounds[0]+1:
                bounds[0] += 1
                bounds[1] -= 1
                self.changeDir(_dir)
            elif _dir == [0, 1] and j == bounds[1]:
                self.changeDir(_dir)
            elif _dir == [0, -1] and j == bounds[0]:
                self.changeDir(_dir)
            elif _dir == [1, 0] and i == bounds[1]:
                self.changeDir(_dir)
            
            i += _dir[0]
            j += _dir[1]
        return A