class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        empty_spaces = 1

        if len(flowerbed) == 1:
            if flowerbed[0] == 0 or n == 0:
                return True
            else:
                return False

        for plot in flowerbed:
            if plot == 0:
               empty_spaces += 1
               if empty_spaces == 3:
                   n -= 1
                   empty_spaces = 1
            else:
                empty_spaces = 0
        
        if empty_spaces == 2:
            n -= 1

        if n <= 0:
            return True
        else:
            return False