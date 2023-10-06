class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        
        threes = n//3
        rest = n%3

        print(threes)
        print(rest)
        
        if rest == 1:
            rest = 4
            if threes > 0:
                threes -= 1

        if rest == 0:
            rest = 1
            
        
        return 3**threes * rest