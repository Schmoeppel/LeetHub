class Solution {
public:
    bool isReachableAtTime(int sx, int sy, int fx, int fy, int t) {
        if(sx==fx and sy==fy and t==1){
            return false;
        }
        int x_diff = abs(fx-sx);
        int y_diff = abs(fy-sy);
        int max_diff, min_diff;

        if (x_diff > y_diff){
            max_diff = x_diff;
            min_diff = y_diff;
        }
        else{
            min_diff = x_diff;
            max_diff = y_diff;
        }
        return t>= min_diff + max_diff-min_diff;

    }
};