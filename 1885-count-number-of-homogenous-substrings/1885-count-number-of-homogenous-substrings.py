class Solution:
    def countHomogenous(self, s: str) -> int:
        total_cnt = 0
        prev_char = s[0]
        cnt = 0
        for char in s:
            if char == prev_char:
                cnt += 1
            else:
                total_cnt += sum(range(cnt+1))
                cnt = 1
            prev_char = char
        
        cnt+=1
        total_cnt += sum(range(cnt))
        
        return total_cnt % (10**9 + 7)

