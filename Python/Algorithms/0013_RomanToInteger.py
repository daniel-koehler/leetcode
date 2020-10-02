class Solution:
    def romanToInt(self, s: str) -> int:
        sym_to_val = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1        
        }
        num = 0
        prev = 0
        for c in s[::-1]:
            value = sym_to_val[c]
            if value < prev:
                num -= value
            else:
                num += value
            prev = value
        
        return num