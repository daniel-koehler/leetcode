# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Two pass
# Time:  O(L) where L is the length of the list
# Space: O(1)
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p1 = head
        length = 0
        while p1:
            p1 = p1.next
            length += 1
        
        d = p1 = ListNode(next=head)
        for _ in range(length-n):
            p1 = p1.next
        
        p1.next = p1.next.next

        return d.next

# Single pass
# Time:  O(L) where L is the length of the list
# Space: O(1)
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        d = ListNode(next=head)
        p1 = p2 = d
        
        for _ in range(n+1):
            p1 = p1.next
            
        while p1:
            p1 = p1.next
            p2 = p2.next
        
        p2.next = p2.next.next
        return d.next