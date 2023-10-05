class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        thresh = len(nums)/3

        output = []
        
        for num in set(nums):
            if nums.count(num) > thresh:
                output.append(num)

        return output