# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
            
        buffer_list = []
        while head:
            buffer_list.append(head.val)
            head = head.next


        head = ListNode(buffer_list[-1], None)
        origin_head = head
        for element in reversed(buffer_list[:-1]):
            head.next = ListNode(element, None)
            head = head.next

        return origin_head