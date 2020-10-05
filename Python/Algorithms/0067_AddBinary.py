class Solution:

    def addBinary(self, a: str, b: str) -> str:
        la, lb = len(a), len(b)
        lmax = max(la, lb)
        a = a.zfill(lmax)
        b = b.zfill(lmax)
        print(a,b)
        carry = 0
        res = ""
        for i in range(max(la, lb)-1, -1, -1):
            _sum = carry + int(a[i]) + int(b[i])
            if _sum < 2:
                res = str(_sum) + res
                carry = 0
            elif _sum == 2:
                res = "0" + res
                carry = 1
            else:
                res = "1" + res
                carry = 1
        if carry:
            res = "1" + res
        return res

class Solution:
    
    def addBinary(self, a: str, b: str) -> str:
        la, lb = len(a), len(b)
        lmax = max(la, lb)
        a = a.zfill(lmax)
        b = b.zfill(lmax)
        carry = 0
        res = ""
        for i in range(max(la, lb)-1, -1, -1):
            _sum = carry + int(b[i]) + int(a[i]) 
            res = str(_sum % 2) + res
            carry = _sum >= 2
        if carry:
            res = "1" + res
        return res