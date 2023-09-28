# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        l3 = head
        overflow = 0

        while True:
            if l1 != None:
                l3.val += l1.val
                l1 = l1.next
            if l2 != None:
                l3.val += l2.val
                l2 = l2.next
            l3.val += overflow
            if l3.val >= 10:
                l3.val -= 10
                overflow = 1
            else:
                overflow = 0
            
            if l1 == None and l2 == None and overflow == 0:
                return head

            l3.next = ListNode()
            l3 = l3.next