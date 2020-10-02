# Cheat with built-in find()
class SolutionFind:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: 
            return 0
        
        return haystack.find(needle)
  
# Sliding window
# Time:  O(n)
# Space: O(1)
class SolutionSlidingWindow:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: 
            return 0   
        l_needle = len(needle)
        l_haystack = len(haystack)
        # Note that we could also iterate over range(l_haystack) as index bounds are checked for slices.
        for i in range(l_haystack-l_needle+1):  
            if haystack[i:i+l_needle] == needle:
                return i
        return -1