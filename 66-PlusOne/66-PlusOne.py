# Last updated: 1/1/2026, 12:14:11 PM
1class Solution:
2    def plusOne(self, digits: List[int]) -> List[int]:
3        return [int(c) for c in str(int("".join(map(str, digits))) + 1)]
4
5        
6
7
8
9        