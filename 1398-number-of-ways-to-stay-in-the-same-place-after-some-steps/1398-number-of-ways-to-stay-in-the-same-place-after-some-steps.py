class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:

        if arrLen == 1:
            return 1

        dp = [0]*(arrLen+2)
        dp[1] = 1
        dp[2] = 1

        #print(dp)
        result_cnt = 3
        for _ in range(steps-1):
            dp_old = dp.copy()
            for idx in range(1,min(result_cnt+1, arrLen+1)):
                dp[idx] = dp_old[idx-1] + dp_old[idx] + dp_old[idx+1]
            result_cnt += 1
            #print(dp)

        return dp[1]%(10**9+7)
