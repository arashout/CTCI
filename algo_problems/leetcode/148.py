class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        (a, b) = self.split(head)
        l1 = self.sortList(a)
        l2 = self.sortList(b)
        
        return self.merge(l1, l2)
        
    def split(self, head: ListNode) -> (ListNode, ListNode):
        slow = head
        fast = head
        prev = None
        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None # Cut off lists from each other
        return (head, slow)
    
    def merge(self, a: ListNode, b: ListNode) -> ListNode:
        dummy = ListNode(0)
        tail = dummy
        while a or b:
            if a is None:
                tail.next = b
                b = b.next
            elif b is None:
                tail.next = a
                a = a.next
            else:
                if a.val < b.val:
                    tail.next = a
                    a = a.next
                else:
                    tail.next = b
                    b = b.next
            tail = tail.next
        
        return dummy.next


l = [4, 3, 2, 5]
dummy = ListNode(0)
tail = dummy
for n in l:
    tail.next = ListNode(n)
    tail = tail.next

s = Solution()
head = s.sortList(dummy.next)

while head:
    print(head.val)
    head = head.next