class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        flips = 0
        ones = 0
        max_ones = 0

        while right < len(nums):
            if nums[right] == 1 or flips < k:
                if nums[right] == 0:
                    flips += 1
                right += 1
                ones += 1
            else:
                if nums[left] == 0:
                    flips -= 1
                left += 1
                ones -= 1
            max_ones = max(ones, max_ones)
        
        return max_ones
                

