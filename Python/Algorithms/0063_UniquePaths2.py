# Dynamic programming - Bottom-up
# Time:  O(n*m)
# Space: O(n*m)
# Note: one could also use obstacleGrid for the dp memoization to obtain
# space complexity of O(1)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        # Initialize memory
        dp = [[0 for j in range(n)] for i in range(m)]
        dp[0][0] = int(not obstacleGrid[0][0])
        for i in range(1, n):
            dp[0][i] = int(dp[0][i-1] and not obstacleGrid[0][i])
        for i in range(1, m):
            dp[i][0] = int(dp[i-1][0] and not obstacleGrid[i][0])

        if n == 1 or m == 1:
            return dp[m-1][n-1]
        
        # Calculate number of paths for each field
        for i in range(1,m):
            for j in range(1,n):
                if not obstacleGrid[i][j]:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[i][j]