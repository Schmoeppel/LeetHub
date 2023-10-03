class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        count_dict = {}

        for num in nums:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1

        good_pairs = 0

        for num, count in count_dict.items():
            for i in range(count):
                good_pairs += i

        return good_pairs