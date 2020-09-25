# By row
# Time:  O(n)
# Space: O(n)
# Assign characters to their row in the ZigZag pattern
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        rows = ['' for _ in range(numRows)]
        curr_row = 0
        down = True
        for c in s:
            rows[curr_row] += c  
            curr_row = curr_row + 1 if down else curr_row - 1
            # Toggle flag
            if (curr_row == numRows - 1) or (curr_row == 0):
                down = not down

        return ''.join(rows)

# By index
# Time:  O(n)
# Space: O(1) if result is not considered
# Utilize the fact that the indices of
# - Row 0           are k * (numRows * 2 - 2)
# - Row (numRows-1) are k * (numRows * 2 - 2) + numRows - 1
# - Inner row i     are k * (numRows * 2 - 2) +/- i
class Solution1:
    def convert(self, s: str, numRows: int) -> str:
        #if numRows == 1: return s
        res = ''
        stride = 2 * numRows - 2
        for i in range(numRows):
            j = 0
            while(j + i < len(s)):
                res += s[i + j]
                if (i != 0) and (i != numRows-1) and (j + stride - i < len(s)):
                    res += s[j - i + stride]
                j += stride

        return res

print(Solution().convert("PAYPALISHIRING", numRows = 3))