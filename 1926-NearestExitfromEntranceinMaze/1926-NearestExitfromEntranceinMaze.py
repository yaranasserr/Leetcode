import collections

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])

        # Initialize the queue and add the entrance
        q = collections.deque()
        q.append((entrance[0], entrance[1], 0))  # (row, col, steps)

        # Directions: Right, Left, Down, Up
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # Mark the entrance as visited
        maze[entrance[0]][entrance[1]] = '+'

        while q:
            r, c, steps = q.popleft()

            # Check if it's at the border and not the entrance
            if (r == 0 or r == m-1 or c == 0 or c == n-1) and (r != entrance[0] or c != entrance[1]):
                return steps

            # Explore the neighbors
            for dr, dc in directions:
                row, col = r + dr, c + dc

                # Check if the new position is within bounds and not visited
                if 0 <= row < m and 0 <= col < n and maze[row][col] == '.':
                    maze[row][col] = '+'  # Mark the cell as visited
                    q.append((row, col, steps + 1))  # Add the neighbor to the queue with incremented steps

        return -1  # Return -1 if no exit is found
