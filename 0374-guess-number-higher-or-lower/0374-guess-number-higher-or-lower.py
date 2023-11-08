# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lower_limit = 1
        upper_limit = n+1
        my_guess = 0
        while True:
            my_guess = (upper_limit+lower_limit)//2
            result = guess(my_guess)
            if result == -1:
                upper_limit = my_guess
            elif result == 1:
                lower_limit = my_guess
            else:
                break
        
        return my_guess
