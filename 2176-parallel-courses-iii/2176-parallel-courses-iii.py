class Solution:
    
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        if relations == []:
            return max(time)
        def topological_sort(graph):
            def dfs(node):
                visited.add(node)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        dfs(neighbor)
                result.insert(0, node)

            visited = set()
            result = []

            nodes = list(graph.keys())
            
            for node in nodes:
                #print(node)
                if node not in visited:
                    dfs(node)

            return result

        #relations = [[1,5],[2,5],[3,5],[3,4],[4,5]]

        # Create a graph using a dictionary
        graph = defaultdict(list)
        for u, v in relations:
            graph[u].append(v)

        dependencies = defaultdict(list)
        for u, v in relations:
            dependencies[v].append(u)
        
        #print(graph)
        #print(dependencies)

        topological_order = topological_sort(graph)
        #print(topological_order)

        time_needed = defaultdict()

        for idx, item in enumerate(topological_order):
            if item not in dependencies:
                time_needed[item] = time[item-1]
            else:
                time_needed[item] = (time[item-1] + max([time_needed[x] for x in dependencies[item]]))
        
        #def get_min_time(course, topological_order, )
        #print(time_needed)

        return max(max(time), max(time_needed.values()))




        