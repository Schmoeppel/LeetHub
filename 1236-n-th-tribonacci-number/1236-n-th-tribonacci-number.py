class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1

        t0 = 0
        t1 = 1
        t2 = 1

        t_new = 0
        for _ in range(n-2):
            t_new = t0+t1+t2
            t0 = t1
            t1 = t2
            t2 = t_new
        return t_new