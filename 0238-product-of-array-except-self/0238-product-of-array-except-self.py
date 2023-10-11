import numpy as np
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        output = np.ones(length, dtype=np.int32)
        #factor = np.ones(length, dtype=np.int32)

        for i in range(length):
            factor = np.ones(length, dtype=np.int32) * nums[i]
            factor[i] = 1
            output = output * factor

        return output