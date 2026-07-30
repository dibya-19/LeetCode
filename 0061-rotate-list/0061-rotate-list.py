# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head

        l = 1
        last = head
        while last.next != None:
            last = last.next
            l += 1

        k %= l
        curr = head
        
        for i in range(l-k-1):
            curr = curr.next

        last.next = head
        head = curr.next
        curr.next = None

        return head

