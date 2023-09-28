class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        new_nums = []
        for num in nums:
            if num % 2 == 0:
                new_nums.insert(0, num)
            else:
                new_nums.append(num)
        
        return new_nums