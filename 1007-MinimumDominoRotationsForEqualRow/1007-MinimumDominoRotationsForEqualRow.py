# Last updated: 5/3/2025, 2:54:24 PM
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        # 1 - find most common element in both arrays
        from collections import Counter

        def most_common(arr):
            counter = Counter(arr)
            most_common_num, most_common_freq = counter.most_common(1)[0]
            return most_common_num, most_common_freq

        t_num, t_freq = most_common(tops)
        b_num, b_freq = most_common(bottoms)

        swaps = 0 

        for i, (top_val, bottom_val) in enumerate(zip(tops, bottoms)):
            if t_freq > b_freq:
                maximum = t_num
                if tops[i] != maximum and bottom_val == maximum:
                    swaps += 1 
                    tops[i] = maximum

            else:
                maximum = b_num 
                if bottoms[i] != maximum and top_val == maximum:
                    swaps += 1 
                    bottoms[i] = maximum
                    

        if all(element == maximum for element in tops) or all(element == maximum for element in bottoms):
            return swaps
        return -1 
       
        



        

     


        
        

        