class Solution:
    def countVowelPermutation(self, n: int) -> int:        
        dp = [1,1,1,1,1]

        for i in range(n-1):
            dp = [dp[1]+dp[2]+dp[4],dp[0]+dp[2],dp[1]+dp[3],dp[2],dp[2]+dp[3]]

        return sum(dp)%(10**9 + 7)