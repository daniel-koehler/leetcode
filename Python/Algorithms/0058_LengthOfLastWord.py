class Solution:
    
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        word_encountered = False
        for i in range(len(s)-1, -1, -1):
            if s[i] != ' ':
                word_encountered = True
                length += 1
            elif word_encountered:
                break
        return length

class SolutionBuiltIn:
    
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        return 0 if not words else len(words[-1])