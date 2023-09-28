class Solution:
    def canJump(self, nums: List[int]) -> bool:
        idx = len(nums)-1
        jump_dis = 0

        if idx == 0:
            return True

        while True:
            idx -= 1
            jump_dis += 1
            if idx == 0:
                if nums[idx] >= jump_dis:
                    return True
                else:
                    return False
            if nums[idx] >= jump_dis:
                jump_dis = 0


        