# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        dummy = ListNode()
        pnew = dummy

        while p1 and p2:
            if p1.val <= p2.val:
                pnew.next = ListNode(p1.val)
                p1 = p1.next 
            else:
                pnew.next = ListNode(p2.val)
                p2 = p2.next

            pnew = pnew.next
        

        if p2:
            pnew.next = p2
        
        if p1:
            pnew.next = p1


        




        return dummy.next
