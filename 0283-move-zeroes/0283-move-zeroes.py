class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''length = len(nums)
        if length == 1:
            return

        left = 0
        right = 0'''

        for zero_idx, zero in enumerate(nums):
            if zero == 0:
                for non_zero_idx in range(zero_idx, len(nums)):
                    if nums[non_zero_idx] != 0:
                        nums[zero_idx] = nums[non_zero_idx]
                        nums[non_zero_idx] = 0
                        break


                

'''        while True:
            while left < length:
                if nums[left] == 0:
                    break
                left += 1
            if left >= length:
                break
            right = left+1
            while right < length:
                if nums[right] != 0:
                    nums[left] = nums[right]
                    nums[right] = 0
                    break
                right += 1
        
        return'''


        