# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head1 = list1
        head2 = list2
        if head1 == None:
            return head2
        elif head2 == None:
            return head1
        
        else:
            curr1 = head1
            curr2 = head2
            dummy = ListNode()
            tail = dummy
            while curr1 != None and curr2 != None:

                if curr1.val <= curr2.val:
                    tail.next = curr1
                    curr1 = curr1.next
                else:
                    tail.next = curr2
                    curr2 = curr2.next

                tail = tail.next

            if curr1 != None:
                tail.next = curr1

            else:
                tail.next = curr2
        return dummy.next

        

        