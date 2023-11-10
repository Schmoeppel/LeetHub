class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        nums = []

        connections = {}

        
        for pair in adjacentPairs:

            item1 = pair[0]
            item2 = pair[1]
            if item1 not in connections:
                connections[item1] = [item2]
            else:
                connections[item1].append(item2)
            if item2 not in connections:
                connections[item2] = [item1]
            else:
                connections[item2].append(item1)

        for key in connections:
            if len(connections[key]) == 1:
                start_key = key
                break

        nums = [start_key]
        last_key = start_key
        next_key = connections[start_key][0]
        while True:
            if len(connections[next_key]) == 1:
                nums.append(next_key)
                break
            else:
                nums.append(next_key)
                if connections[next_key][0] != last_key:
                    last_key = next_key
                    next_key = connections[next_key][0]
                else:
                    last_key = next_key
                    next_key = connections[next_key][1]
            
        return nums
            
            
