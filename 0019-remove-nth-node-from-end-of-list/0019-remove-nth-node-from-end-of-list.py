# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        if not head:
            return head
        count = 1
        curr = head
        while curr and curr.next:
            curr = curr.next
            count += 1

        if count == n:
            return head.next

        k = count - n
        temp = head
        for i in range(k-1):
            temp = temp.next
        temp.next = temp.next.next
        return head
