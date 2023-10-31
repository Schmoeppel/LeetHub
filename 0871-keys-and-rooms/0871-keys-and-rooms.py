class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque()
        queue.append(0)
        visited = set()
        while queue:
            cur_key = queue.popleft()
            visited.add(cur_key)
            for key in rooms[cur_key]:
                if key not in visited:
                    queue.append(key)

        return len(visited) == len(rooms)

        