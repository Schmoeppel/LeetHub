# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head.next:
            return None

        single_ptr = head
        double_ptr = head

        while double_ptr != None:
            if double_ptr.next:
                double_ptr = double_ptr.next
            else:
                single_ptr.next = single_ptr.next.next
                return head
            if double_ptr.next:
                double_ptr = double_ptr.next
            else:
                single_ptr.next = single_ptr.next.next
                return head
            
            if not double_ptr.next:
                single_ptr.next = single_ptr.next.next
                return head
            
            single_ptr = single_ptr.next
        