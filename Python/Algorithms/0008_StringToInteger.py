INT_MIN = -2**31
INT_MAX = 2**31 - 1

# Just add conditions for each test case
class SolutionSwitchCase:
    def myAtoi(self, s: str) -> int:
        num = 0
        sign = 0
        number_started = False
        for c in s:
            if 48 <= ord(c) <= 57:
                number_started = True
                num = num * 10 + int(c)
            elif number_started:
                break
            elif c == '-' and not sign:
                sign = -1
            elif c == '+' and not sign:
                sign = 1
            elif c == ' ' and not sign:
                continue
            else:
                return 0
        
        if not sign: sign = 1
        num = sign * num
        if INT_MIN > num: return INT_MIN
        elif INT_MAX < num: return INT_MAX
        else: return num

# Use a regular expression instead
class SolutionRegex:
    import re
    def myAtoi(self, s: str) -> int:
        if r := re.match(r"[ ]*[+-]?[\d]+", s):
            num = int(r.group(0))
        else:
            return 0
        
        if INT_MIN > num: return INT_MIN
        elif INT_MAX < num: return INT_MAX
        else: return num