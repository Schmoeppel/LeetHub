class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = float("-inf")
        sum = 0

        for i in range(k):
            sum += nums[i]

        max_sum = sum

        for i in range(k, len(nums)):
            sum = sum + nums[i] - nums[i-k]
            max_sum = max(sum, max_sum)

        return max_sum/k


