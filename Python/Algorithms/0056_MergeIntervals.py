# Sorting
# Time:  O(n log(n))
# Space: O(n), timsort in Python requires a temporary array of size n//2 in the worst-case,
# although sorting lists in place.
class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: 
            return []
        
        intervals.sort()
        merged_intervals = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= merged_intervals[-1][1]:
                merged_intervals[-1][1] = max(intervals[i][1], merged_intervals[-1][1])
            else:
                merged_intervals.append(intervals[i])
                
        return merged_intervals

#TODO(daniel): graph-based approach