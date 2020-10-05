# Dynamic programming - Bottom-up
# Time:  O(n)
# Space: O(n)
class SolutionDynamicProgramming:
    
    def climbStairs(self, n: int) -> int:
        # Trivial case
        if n == 1:
            return 1
        
        # Initialize memory
        dp = [0 for i in range(n)]
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
            
        return dp[n-1]

# Fibonacci sequence
# Time:  O(n)
# Space: O(1)
# The number of possible paths actually relates to the Fibonacci sequence, as can be seen 
# from the statement dp[i] = dp[i-1] + dp[i-2]. Thus we can just return the corresponding number 
# of the Fibonacci sequence
class SolutionFibonacci:
    
    def climbStairs(self, n: int) -> int:
        a, b = 0, 1
        for i in range(n):
            a, b = b, a+b
        return b

# Alternative approaches:
# - Recursion / Backtracking
# - Calculating the Fibonacci number by Binet's method or the closed-form expression