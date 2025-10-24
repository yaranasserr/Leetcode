# Last updated: 10/24/2025, 12:32:40 PM
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        column = ord(coordinates[0])
        row = int(coordinates[1])
        
        return (column - row) % 2 == 1