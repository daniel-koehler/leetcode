# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Iterate over the input linked lists and keep track of the carry.
# Time:  O(max(m,n))
# Space: O(max(m,n))
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1, n2 = l1, l2
        head = digit = ListNode()
        carry = 0
        while True:
            
            if n1:
                v1 = n1.val
                n1 = n1.next
            else:
                v1 = 0
                
            if n2:
                v2 = n2.val
                n2 = n2.next
            else:
                v2 = 0
                
            _sum = v1 + v2 + carry
            digit.val = _sum % 10
            carry = _sum // 10
            
            if not (n1 or n2 or carry):
                return head
            
            digit.next = digit = ListNode()