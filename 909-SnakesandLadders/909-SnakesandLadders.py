# Last updated: 5/31/2025, 12:31:28 PM
from collections import deque
from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        length = len(board)  # The length of the board
        board.reverse()  # Reverse the board for easier processing

        # Helper function to convert a square number to row and column position
        def intToPos(square):
            r = (square - 1) // length  # Row position (0-indexed)
            c = (square - 1) % length  # Column position (0-indexed)
            if r % 2 == 1:  # If the row is odd, reverse the column order
                c = length - 1 - c
            return [r, c]

        # BFS setup
        q = deque()  # Queue for BFS
        q.append([1, 0])  # Start at square 1 with 0 moves
        visit = set()  # Set to track visited squares

        while q:
            square, moves = q.popleft()  # Get the current square and the number of moves

            # Try rolling a dice (1 to 6)
            for i in range(1, 7):
                nextSquare = square + i  # Move to the next square

                # Convert the next square to row and column
                r, c = intToPos(nextSquare)

                # If there's a ladder or snake, move to the destination square
                if board[r][c] != -1:
                    nextSquare = board[r][c]

                # If we've reached the last square, return the number of moves
                if nextSquare == length * length:
                    return moves + 1

                # If the next square hasn't been visited, add it to the queue
                if nextSquare not in visit:
                    visit.add(nextSquare)
                    q.append([nextSquare, moves + 1])

        return -1  # If no solution, return -1
