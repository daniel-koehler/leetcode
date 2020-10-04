# Dynamic programming - Bottom-up
# Time:  O(n*m)
# Space: O(n*m)
class SolutionDynamicProgramming:
    def uniquePaths(self, m: int, n: int) -> int:
        # Trivial case        
        if n == 1 or m == 1:
            return 1
        
        # Initialize memory
        dp = [[1 if i == 0 or j == 0 else 0 for j in range(n)] for i in range(m)]
        
        # Calculate number of paths for each field
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[i][j]

# Dynamic programming - Bottom-up
# Time:  O(n*m)
# Space: O(n)
# Has only linear space complexity
class SolutionDynamicProgrammingOptimized:
    def uniquePaths(self, m: int, n: int) -> int:
        # Trivial case        
        if n == 1 or m == 1:
            return 1
        
        # Initialize memory
        dp = [1 for i in range(n)]        
        
        # Calculate number of paths for each field
        for i in range(1,m):
            for j in range(1,n):
                dp[j] += dp[j-1]
        return dp[j]

# Solve the underlying combinatorial problem:
# Each path consists of m-1 'down' and n-1 'right' moves, such that the path length is m+n-2. 
# The number of paths is equal to the number of ways to choose m-1 (or n-1) moves from a path
# of length n+m-2, i.e. (n+m-2) choose (m-1)
class SolutionCombinatorics:
    def uniquePaths(self, d1: int, d2: int) -> int:
        
        n = d1 + d2 - 2     # Length of path
        r = d1 - 1          # Number of moves to choose
        return math.comb(n,r)