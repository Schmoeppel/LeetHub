class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if len(nums) == 0:
            return [-1,-1]

        max_idx = len(nums)
        min_idx = 0
        idx = -1
        
        while True:
            last_idx = idx
            idx = (max_idx+min_idx) //2

            if last_idx == idx:
                return [-1, -1]
    
            if nums[idx] < target:
                min_idx = idx
            elif nums[idx] > target:
                max_idx = idx
            if nums[idx] == target:
                left = idx
                right = idx
                while left >= 0 and nums[left] == target:
                    left -= 1
                while right <= (len(nums)-1) and nums[right] == target:
                    right += 1 
                left += 1
                right -= 1 
                return [left, right]
            
            if max_idx <= min_idx:
                return [-1, -1]

            


