class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #ks = list(range(1, max(piles)+1))
        
        left = 1
        right = max(piles)

        def hours_to_finish(speed):
            hours = 0
            for pile in piles:
                hours += ceil(pile/speed)
            return hours

        while left<right:
            k = (left+right)//2
            hours = hours_to_finish(k)
            if hours > h:
                left = k+1
            else:
                right = k

        return left