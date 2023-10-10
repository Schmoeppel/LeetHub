class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        result = [False]*len(candies)
        for i, candy in enumerate(candies):
            if candy+extraCandies >= max_candy:
                result[i] = True
        
        return result