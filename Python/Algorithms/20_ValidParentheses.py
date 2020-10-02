# Using a stack
# Time:  O(n)
# Space: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(': ')', '[': ']', '{': '}'}
        o = []
        for c in s:
            if c in brackets:
                o.append(brackets[c])
            elif not o or o.pop() != c:
                return False      
        return not o