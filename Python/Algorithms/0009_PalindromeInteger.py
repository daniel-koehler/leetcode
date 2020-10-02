# Iterate over digits
# Time:  O(log(x))
# Space: O(1)
# Reverse the integer as in problem #7.
class SolutionByDigit:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        x_rev = 0
        while x:
            x, digit = divmod(x, 10)
            x_rev = x_rev * 10 + digit

        return x == x_rev

# Reverse string
# Time:  O(log(x))
# Space: O(log(x))
# As in problem #7 use the reversed string of an integer.
class SolutionByString:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]