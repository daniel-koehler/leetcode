# Brute force
# Time:  O(n^3)
# Space: O(1)
class SolutionBruteForce:
    def longestPalindrome(self, s: str) -> str:
        s_len = len(s)
        max_len = 0
        res = ''
        for i in range(s_len):
            for j in range(i, s_len):
                sub = s[i:j+1]
                if sub == sub[::-1] and max_len < len(sub):
                    max_len = len(sub)
                    res = sub
        return res

# Expand around center
# Time:  O(n^2)
# Space: O(1)
# Expand a slice of the string around each possible center of a palindrome.
# As the length of a palindrome can be both even and uneven there are 2*n-1 such centers.
class SolutionExpandCenter:
    def expand_center(self, s: str, left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left:right]

    def longestPalindrome(self, s: str) -> str:
        s_len = len(s)
        res = ''
        for i in range(s_len):
            uneven = self.expand(s, i, i)
            even   = self.expand(s, i, i+1)
            res = max(res, even, uneven, key=len)

        return res