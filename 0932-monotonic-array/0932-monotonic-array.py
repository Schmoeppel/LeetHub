class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        
        direction = []
        for idx in range(1, len(nums)):
            direction.append(nums[idx]-nums[idx-1])
        
        max_val = max(direction)
        min_val = min(direction)

        if max_val > 0 and min_val < 0:
            return False
        else:
            return True
        
        '''direction = nums[-1] - nums[0]
        cur_direction = 0

        for idx in range(1, len(nums)):
            cur_direction = nums[idx] - nums[idx-1]
            if cur_direction <= 0 and direction <= 0:
                pass
            elif cur_direction >= 0 and direction >= 0:
                pass
            else:
                return False
        
        return True'''