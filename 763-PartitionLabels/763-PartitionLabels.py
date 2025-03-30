# Last updated: 3/30/2025, 4:37:15 PM
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # two pointers
        # Precompute the last occurrence of each character in s
        last ={c:i for i,c in enumerate(s)}
        #{'a': [2], 'b': [3], 'c': [5]}
    
        #track the farthest last occurrence 
        start = 0 
        end = 0
        res = []
        for i,c in enumerate(s):
            end = max(end,last[c]) 
            if i == end :
                res.append(end-start+1)
                start =i+1

        return res





 
       

        

            


            


        