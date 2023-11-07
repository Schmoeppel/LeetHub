class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time_till_arrival = [0]*len(dist)

        for i in range(len(dist)):
            time_till_arrival[i] = (dist[i] + speed[i]-1)//speed[i]
        
        time_till_arrival.sort()

        for time, monster_time in enumerate(time_till_arrival):
            if time >= monster_time:
                return time
        
        return len(dist)

        return 0