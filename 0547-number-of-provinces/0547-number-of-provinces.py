class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        self.visited = set()

        def check_province_from(start_city):
            queue = deque([])
            queue.append(isConnected[start_city])
            self.visited.add(start_city)
            while queue:
                cur_city = queue.popleft()
                for city, connection in enumerate(cur_city):
                    if connection:
                        if city not in self.visited:
                            self.visited.add(city)
                            queue.append(isConnected[city])
        
        all_cities = list(range(len(isConnected)))

        res = 0
        while len(self.visited) < len(isConnected):
            remaining_cities = [x for x in all_cities if x not in self.visited]
            check_province_from(remaining_cities[0])
            res += 1

        return res

            
        
