# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Single pass with new lists
# Time:  O(n)
# Space: O(n)
# Create a linked list for both partitions respectively and concatenate them 
# after adding all elements of the original linked list
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        h1 = h2 = p1 = p2 = None
        curr = head
        while curr:
            if curr.val < x:
                if not h1:
                    h1 = p1 = ListNode(curr.val)
                else:
                    p1.next = p1 = ListNode(curr.val)
            else:
                if not h2:
                    h2 = p2 = ListNode(curr.val)
                else:
                    p2.next = p2 = ListNode(curr.val)
                    
            curr = curr.next
        
        if not h1:
            return h2
        elif h2:
            p1.next = h2
        return h1

# Single pass, two pointers
# Time:  O(n)
# Space: O(1)
# Use two pointers to rearrange the links of the original list.
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        
        h1 = l1 = ListNode()
        h2 = l2 = ListNode()
        while head:
            if head.val < x:
                l1.next = l1 = head
            else:
                l2.next = l2 = head      
            head = head.next
        
        l2.next = None
        l1.next = h2.next
        return h1.next