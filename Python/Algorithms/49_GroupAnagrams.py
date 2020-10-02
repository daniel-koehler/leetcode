# Group by sorted strings
# Time:  O(n * m * log(m)), we need to sort n strings of length m [sorting: O(m *log(m))]
# Space: O(n * m)
class SolutionSortedString:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:        
        hashmap = {}        
        for string in strs:
            key = "".join(sorted(string))
            if key in hashmap:
                hashmap[key].append(string)
            else:
                hashmap[key] = [string]
                
        return hashmap.values()

# Use collections.defaultdict to simplify the code
class SolutionSortedString2:
    import collections
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:        
        hashmap = collections.defaultdict(list)
        for string in strs:
            hashmap[tuple(sorted(string))].append(string)    
        return hashmap.values()

# Group by character count
# Time:  O(n * m)
# Space: O(n * m)
class SolutionCharacterCount:

    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()