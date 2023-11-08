/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

class Solution {
public:
    int guessNumber(int n) {
        int lower, my_guess, result;
        unsigned int upper;
        lower = 1;
        upper = n;
        upper += 1;
        while(true){
            my_guess = (upper+lower)/2;
            result = guess(my_guess);
            if(result == 0){
                return my_guess;
            }
            else if(result == 1){
                lower = my_guess;
            }
            else{
                upper = my_guess;
            }
        }
    }
};