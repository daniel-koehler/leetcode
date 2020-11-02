# Using sort()
# Time:  O((m+n) log(m+n))
# Space: O(m+n)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:m+n] = nums2
        nums1.sort()

# Two pointers
# Time:  O(m+n)
# Space: O(1)
# Fill nums1 from the back starting with the largest number.
INT_MIN = -2**31
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i1, i2 = m - 1, n - 1
        
        for i in range(m + n - 1, -1, -1):
            n1 = nums1[i1] if i1 >= 0 else INT_MIN
            n2 = nums2[i2] if i2 >= 0 else INT_MIN
            if n2 >= n1:
                nums1[i] = n2
                i2 -= 1
            else:
                nums1[i] = n1
                i1 -= 1