class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #idx = len(nums)-1
        jump_dis = 0

        if len(nums) == 1:
            return True

        for index, item in reversed(list(enumerate(nums))):
            if item >= jump_dis:
                jump_dis = 0
            jump_dis += 1
        
        if nums[0] >= jump_dis:
            return True
        else:
            return False

        '''while True:
            idx -= 1
            jump_dis += 1
            if idx == 0:
                if nums[idx] >= jump_dis:
                    return True
                else:
                    return False
            if nums[idx] >= jump_dis:
                jump_dis = 0'''


        