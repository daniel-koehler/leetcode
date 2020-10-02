# Recursive solution
# Time:  O(log2(n))
class Solution:
    def myPow(self, x: float, n: int) -> float:
        """ Recursive power function. Restriction: log2(n) must be smaller than maximum recursion depth """ 
        if n < 0:
            return 1 / self.myPow(x, -n)
        elif n == 0:
            return 1
        elif n == 1:    # not strictly necessary but saves one recursion
            return x
        
        n2, rem = divmod(n, 2)
        p2 = self.myPow(x, n2)
        if rem:
            return p2 * p2 * x
        else:
            return p2 * p2