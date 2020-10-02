# Using a stack
# Time:  O(n)
# Space: O(n)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_len = 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)    
                else:
                    max_len = max(i - stack[-1], max_len)            
        return max_len