from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()  # Sort potions for binary search
        n = len(potions)
        result = []
        
        def binary_search(spell: int) -> int:
            left, right = 0, n - 1
            while left <= right:
                mid = (left + right) // 2
                if spell * potions[mid] >= success:
                    right = mid - 1  # Look for a smaller index
                else:
                    left = mid + 1  # Look for a larger index
            return left  # Left points to the first valid potion
        
        for spell in spells:
            index = binary_search(spell)
            result.append(n - index)  # Count successful pairs
        
        return result


# class Solution:
#     def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
#        potions.sort() 
#        results = [[spell * potion for potion in potions] for spell in spells]
#        res = []
#        for row in results:
        
#         for i in range(len(row)) :
#             l,r=0,len(row)-1
#             while l <= r:
#                 m= l+r //2 
#                 if success > m:
#                     l= m-1
#                 elif success < m:
#                     r = m+1
#                 else:
#                     return m 
#         res.append(len(row)-m)

#         return res 

    



        

         


        
        