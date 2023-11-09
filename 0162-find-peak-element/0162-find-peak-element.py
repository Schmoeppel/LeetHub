class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        length = len(nums)
        right = length
        
        while True:
            mid = (left+right)//2
            left_num = nums[mid-1] if mid > 0 else float('-inf')
            right_num = nums[mid+1] if mid < length-1 else float('-inf')
            if left_num < nums[mid] > right_num:
                return mid
            elif left_num > nums[mid]:
                right = mid
            elif right_num > nums[mid]:
                left = mid+1