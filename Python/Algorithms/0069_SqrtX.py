class Solution:

    def mySqrt(self, x: int) -> int:
        return int(x**0.5)

# Binary search
class Solution:
    
    def mySqrt(self, x: int) -> int:

        l, r = 0, x
        while l <= r:
            root = (l + r) // 2
            power = root * root
            if power == x:
                return root
            elif power > x:
                r = root - 1
            elif power < x:
                l = root + 1
        if power > x:
            return root - 1
        return root

