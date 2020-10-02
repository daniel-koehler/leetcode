# Compare one by one
# Time:  O(m+n)
# Space: O(1)
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not (l1 or l2): return None
        ref = head = ListNode()
        while l1 or l2:
            v1 = 2**31 if not l1 else l1.val
            v2 = 2**31 if not l2 else l2.val
            
            if v1 < v2:
                ref.val = v1
                l1 = l1.next
            else:
                ref.val = v2
                l2 = l2.next
            
            if l1 or l2:
                ref.next = ref = ListNode()
        return head