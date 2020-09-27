# Brute force
# Time:  O(n^2)
# Space: O(1)
class SolutionBruteForce:
    def maxArea(self, height: List[int]) -> int:
        l = len(height)
        area = 0
        for i in range(l):
            for j in range(i+1,l):
                area = max(area, (j-i) * min(height[i], height[j]))
        return area

# Two pointer approach
# Time:  O(n)
# Space: O(1)
class SolutionTwoPointerApproach:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        max_area = 0
        while i != j:
            if height[i] <= height[j]:
                max_area = max((j-i) * height[i], max_area)
                i += 1
            else:
                max_area = max((j-i) * height[j], max_area)
                j -= 1
        return max_area