class Solution {
public:
    int countHomogenous(string s) {
        const long long mod = 1e9+7;
        long long total_cnt, length, cnt;
        char prev_char;
        length = s.size();
        prev_char = s[0];
        total_cnt = 0;
        cnt = 0;
        for (int i=0; i<length; i++){
            if (s[i] == prev_char){
                cnt++;
            } else{
                for (int j=1; j<=cnt; j++){
                    total_cnt += j;
                }
                cnt=1;
            }
            prev_char = s[i];
        }
        for (int j=1; j<=cnt; j++){
            total_cnt += j;
        }
        return total_cnt%mod;
    }
};