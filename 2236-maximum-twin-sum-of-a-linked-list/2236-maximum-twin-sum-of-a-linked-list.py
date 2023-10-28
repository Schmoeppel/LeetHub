# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        temp_list = []
        while head:
            temp_list.append(head.val)
            head = head.next

        left = 0
        right = len(temp_list)-1

        max_sum = float("-inf")

        for _ in range(len(temp_list)//2):
            cur_sum = temp_list[left]+temp_list[right]
            max_sum = max(cur_sum, max_sum)
            left += 1
            right -= 1

        return max_sum