# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return

        return_head = ListNode(None)
        new_node = return_head

        while True:
            if list1 == None:
                new_node.val = list2.val
                list2 = list2.next
            elif list2 == None:
                new_node.val = list1.val
                list1 = list1.next
            elif list1.val < list2.val:
                new_node.val = list1.val
                list1 = list1.next
            else:
                new_node.val = list2.val
                list2 = list2.next

            if list1 == None and list2 == None:
                return return_head
            new_node.next = ListNode(None)
            new_node = new_node.next

        return 9999

