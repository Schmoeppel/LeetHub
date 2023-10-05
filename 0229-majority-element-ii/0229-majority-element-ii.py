class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        unique_nums = set(nums)
        thresh = len(nums)/3

        output = []
        
        for num in unique_nums:
            if nums.count(num) > thresh:
                output.append(num)

        return output