class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        element_cnts = dict()

        for num in nums:
            if num in element_cnts:
                element_cnts[num] += 1
            else:
                element_cnts[num] = 1

        output = []
        total_cnt = len(nums)
        for key, value in element_cnts.items():
            if value/total_cnt > (1/3):
                output.append(key)

        return output

