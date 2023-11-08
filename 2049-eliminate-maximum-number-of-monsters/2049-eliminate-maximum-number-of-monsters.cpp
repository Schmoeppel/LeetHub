class Solution {
public:
    int eliminateMaximum(vector<int>& dist, vector<int>& speed) {
        int time_till_arrival[dist.size()];

        for(size_t i = 0; i < dist.size(); i++){
            time_till_arrival[i] = (dist[i] + speed[i]-1)/speed[i];
        }

        const int length = sizeof(time_till_arrival)/sizeof(time_till_arrival[0]);
        std::sort(time_till_arrival, time_till_arrival+length);

        for (int i = 0; i < length; i++){
            if (i >= time_till_arrival[i]){
                return i;
            }
        }

        return length;
    }

    
};