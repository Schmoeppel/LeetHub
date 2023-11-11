class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        stair1 = 0
        stair2 = 0
        stair0 = 0
        for idx in range(len(cost)-1, -1, -1):
            stair0 = cost[idx]+min(stair1, stair2)
            stair2 = stair1
            stair1 = stair0

        return min(stair1, stair2)