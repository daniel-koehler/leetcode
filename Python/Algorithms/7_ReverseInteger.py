INT_MIN = -2**31
INT_MAX = 2**31 - 1

# Straight forward approach
# Time:  O(log(x))
# Space: O(1)
# Create the reversed number digit by digit
class SolutionByDigit:
    def reverse(self, x: int) -> int:
        res = 0
        sign = -1 if (x < 0) else 1
        x = abs(x)
        while x:
            x, digit = divmod(x,10)
            res = res * 10 + digit
        res *= sign
        
        return res if INT_MIN < res < INT_MAX else 0

# Reverse string
# Time:  O(log(x))
# Space: O(log(x))
# Create the reversed number digit by digit
class SolutionByString:
    def reverse(self, x: int) -> int:
        s = str(x)
        if s[0].isdigit():
            x_rev = int(s[::-1])
        else:
            x_rev = - int(s[:0:-1])
        return x_rev if INT_MIN < x_rev < INT_MAX else 0


            
        

print(Solution().reverse(-123))