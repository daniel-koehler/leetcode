# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Options:
# - Divide and conquer
# - sort element by element
# - sort list by list

INT_MAX = 2**31

class Solution:
    def merge2Lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Sort element by element
        if not l1 and l2: return l2
        elif not l2 and l1: return l1
        elif not (l1 or l2): return None
        head = ref = ListNode()
        while True:
            v1 = INT_MAX if not l1 else l1.val
            v2 = INT_MAX if not l2 else l2.val
            
            if v1 < v2:
                ref.val = v1
                l1 = l1.next
            else:
                ref.val = v2
                l2 = l2.next
            
            if l1 or l2:
                ref.next = ref = ListNode()
            else:
                return head           
            
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        res = None
        for i in range(len(lists)):
            res = self.merge2Lists(res, lists[i])
            
        return res


class Solution:
    def merge2Lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Sort element by element
        if not l1 and l2: return l2
        elif not l2 and l1: return l1
        elif not (l1 or l2): return None
        head = ref = ListNode()
        while True:
            v1 = INT_MAX if not l1 else l1.val
            v2 = INT_MAX if not l2 else l2.val
            
            if v1 < v2:
                ref.val = v1
                l1 = l1.next
            else:
                ref.val = v2
                l2 = l2.next
            
            if l1 or l2:
                ref.next = ref = ListNode()
            else:
                return head           
            
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        res = None
        for i in range(len(lists)):
            res = self.merge2Lists(res, lists[i])
            
        return res


INT_MAX = 2**31

class Solution:  
    def get_min(self, lists: List[ListNode]) -> (int, int):
        minimum = INT_MAX
        idx = None
        for i, l in enumerate(lists):
            try:
                if l.val < minimum:
                    idx = i
                    minimum = l.val
            except:
                pass
        return idx, minimum
                
    
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists: return None
        head = curr = ListNode()
        for _ in range(lists.count([])):
            lists.remove([])
        print(lists)
        while True:
            idx, curr.val = self.get_min(lists)
            if not idx:
                return None
            if not lists[idx].next:
                del lists[idx]
            else:
                lists[idx] = lists[idx].next
                
            if lists:
                curr.next = curr = ListNode()
            else:
                return head