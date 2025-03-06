class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        res = 0 
        freq = {}
       
        for r in range(n): 
            for c in range(len(grid[r])):  
                value = grid[r][c]
                freq[value] = 1 + freq.get(value, 0)

        for key , val in freq.items():
            if val == 2 :
                a = key 

        values = list(range(1,(n**2)+1))

        original_values = list(freq.keys())

        difference = [x for x in values if x not in freq]
        res=[a,difference[0]]
        return res
        


        

        