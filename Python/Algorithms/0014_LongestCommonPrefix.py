# Vertical scanning
# Time:  O(S) where S is the number of total characters of all strings in the list
# Space: O(1)
class SolutionHorizontalScanning:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        prefix = ''
        for c in strs[0]:
            cand = prefix + c
            for string in strs[1:]:
                if cand != string[:len(cand)]:
                    return prefix
            else:
                prefix = cand
        
        return prefix


# Horizontal scanning
# Time:  O(S) where S is the number of total characters of all strings in the list
# Space: O(1)
class SolutionVerticalScanning:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        prefix = strs[0]
        for string in strs[1:]:
            p_len = len(prefix)
            while p_len > 0:
                p_len = min(len(prefix), len(string))
                prefix = prefix[:p_len]
                if prefix[:p_len] == string[:p_len]:
                    break
                else:
                    prefix = prefix[:-1]    
        
        return prefix


# Divide and conquer
# Time:  O(S) where S=m * n is the number of total characters m of all n strings in the list
# Space: O(m * log(n))
class SolutionDivideConquer:   
    def commonPrefix(self, str1: str, str2: str) -> str:
        length = min(len(str1), len(str2))
        while length > 0:
            if str1[:length] == str2[:length]:
                return str1[:length]
            length -= 1
        return ''
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s_len = len(strs)
        if s_len == 0: # Trivial case
            return ''
        elif s_len > 2: # Divide
            mid = s_len // 2
            left = self.longestCommonPrefix(strs[:mid])
            right = self.longestCommonPrefix(strs[mid:])
            return self.commonPrefix(left, right)
        elif s_len == 1: # Only one string
            return strs[0]
        else:
            return self.commonPrefix(*strs)


# Binary Search
# Time:  O(S * log(m))
# Space: O(1)
class SolutionBinarySearch:
    
    def isCommonPrefix(self, strs: List[str], length: int):
        for string in strs[1:]:
            if string[:length] != strs[0][:length]:
                return False
        return True
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: # Trivial case
            return ''
        
        min_len = len(min(strs, key=len))
        low, high = 1, min_len
        
        while low <= high:
            middle = (low + high) // 2
            if self.isCommonPrefix(strs, middle):
                low = middle + 1
            else:
                high = middle - 1
        return strs[0][:(low+high)//2]