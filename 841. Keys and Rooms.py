class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        visited.add(0)
        c = rooms[0]

        while c:
            r = c.pop()
            if r not in visited:
                visited.add(r)
                for i in rooms[r]:
                    c.append(i)
        
        return len(visited) == len(rooms)
                
