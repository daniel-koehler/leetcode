# Transpose -> Flip horizontally
# Time:  O(N^2)
# Space: O(1)
class Solution:
    
    def transpose(self, A: List[List[int]]) -> None:
        """ In-place matrix transposition """
        N = len(A)
        for i in range(N):
            for j in range(i+1,N):
                A[i][j], A[j][i] = A[j][i], A[i][j]
    
    def flip2(self, A: List[List[int]]) -> None:
        """ In-place matrix flipping """
        N = len(A)
        for i in range(N):
            for j in range(N//2):
                A[i][j], A[i][N-1-j] = A[i][N-1-j], A[i][j]
                
    def flip(self, A: List[List[int]]) -> None:
        for i in range(len(A)):
            A[i] = A[i][::-1]
        
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.transpose(matrix)
        self.flip(matrix)