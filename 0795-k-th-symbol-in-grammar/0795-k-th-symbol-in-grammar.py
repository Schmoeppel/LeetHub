class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        ks = [k]
        for _ in range(n-1):
            k = (k+1)//2
            ks.append(k)

        #print(ks)

        cur_val = 0
        ks.reverse()
        for cur_k in ks[1:]:
            if cur_k % 2 == 0:
                if cur_val == 0:
                    cur_val = 1
                else:
                    cur_val = 0
            else:
                if cur_val == 0:
                    cur_val = 0
                else:
                    cur_val = 1

        return cur_val