# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_head = head
        if head and head.next:
           even_head = head.next
        else:
            return head
        
        result = odd_head
        even_result = even_head

        odd = True
        cur_head = head.next.next
        while cur_head:
            if odd:
                odd_head.next = cur_head
                odd_head = odd_head.next
                odd = False
            else:
                even_head.next = cur_head
                even_head = even_head.next
                odd = True
            cur_head = cur_head.next

        if odd:
            odd_head.next = None
        else:
            even_head.next = None

        '''test_node = even_result
        while test_node:
            print(test_node.val)
            test_node = test_node.next'''

        odd_head.next = even_result
        return result