# class Solution:
#     def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
#         lst=[]

#         # if index < keys -> mark the index as true return true if true = len of rooms 
#         for index ,keys in enumerate(rooms):
#             for key in keys:
#                 if all(index < value for value in keys):  
#                     lst.append(1)

#         return (len(lst)==len(rooms))
# class Solution:
#     def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
#         visited = set()  # To track visited rooms
#         stack = [0]  # Start with room 0
        
#         while stack:
#             current_room = stack.pop()
#             if current_room not in visited:
#                 visited.add(current_room)
#                 # Add all keys in the current room to the stack
#                 stack.extend(rooms[current_room])
        
#         # If we've visited all rooms, the length of visited should match the total rooms
#         return len(visited) == len(rooms)
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(room):
            visited.add(room)  # Mark the current room as visited
            for key in rooms[room]:  # Visit all rooms accessible with the keys in the current room
                if key not in visited:
                    dfs(key)
        
        visited = set()  # To keep track of visited rooms
        dfs(0)  # Start DFS from room 0
        
        return len(visited) == len(rooms)  # Check if all rooms have been visited
