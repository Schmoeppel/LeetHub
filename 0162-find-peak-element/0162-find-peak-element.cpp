class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int left, right, mid, length;
        long left_num, right_num, mid_num;
        length = nums.size();
        left = 0;
        right = length;

        while(true){
            mid = (left+right)/2;
            if (mid > 0){
                left_num = nums[mid-1];
            }else{
                left_num = numeric_limits<long>::min();
            }

            if (mid < length-1){
                right_num = nums[mid+1];
            }else{
                right_num = numeric_limits<long>::min();
            }

            mid_num = nums[mid];

            if (left_num < mid_num && right_num < mid_num){
                return mid;
            }
            else if (left_num > mid_num){
                right = mid;
            }
            else{
                left = mid+1;
            }
        }
        
    }
};