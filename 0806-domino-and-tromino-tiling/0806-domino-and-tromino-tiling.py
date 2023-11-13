class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 5
        t1 = 1
        t2 = 2
        t3 = 5
        for i in range(n-3):
            t_new = t3*2+t1
            t1 = t2
            t2 = t3
            t3 = t_new
        return t3 % (10**9+7)