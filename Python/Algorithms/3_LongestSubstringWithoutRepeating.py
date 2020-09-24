# Brute force
# Time:  O(n^3)
# Space: O(1) 
# Check all possible substrings (O(n^2)) subsequently and check if there are no duplicate characters (O(n))
class SolutionBruteForce:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s = list(s)
        s_len = len(s)
        max_len = min(s_len, 1)
        
        for i in range(s_len):
            for j in range(i+1, s_len):
                if s[j] in s[i:j]:
                    break
                else:
                    max_len = max(max_len, len(s[i:j+1]))

        return max_len

# Sliding window
# Time:  O(n)
# Space: O(m) where m is the size of the character set
# Use a sliding window of increasing size. A hashmap is used to store char:index pairs that can be used to 
# check whether a new character is already within the window. If so the window is shifted by one.
class SolutionSlidingWindow:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_len = len(s)
        max_len = i = j = 0
        char_set = {}
        while i < s_len and j < s_len:
            new_char = s[j]
            if new_char not in char_set:
                char_set[new_char] = j
                j += 1
                max_len = max(max_len, j-i)
            else:
                del char_set[s[i]]
                i += 1

        return max_len

# Sliding window
# Time:  O(n)
# Space: O(m)
# Again use a sliding window, but now i is updated to the position after the first occurrence of a repeated character.
class SolutionSlidingWindowOptimized:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = i = j = 0
        char_set = {}
        for j, new_char in enumerate(s):
            if new_char in char_set:
                i = max(char_set[new_char] + 1, i)  # only update i if the previous occurrence of new_char is within the current window
            max_len = max(max_len, j-i+1)
            char_set[new_char] = j
            
        return max_len

s = SolutionSlidingWindowOptimized()
print(s.lengthOfLongestSubstring("pwwkew"))