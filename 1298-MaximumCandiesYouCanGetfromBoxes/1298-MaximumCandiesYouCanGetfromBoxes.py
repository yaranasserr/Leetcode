# Last updated: 6/3/2025, 4:19:32 PM
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n = len(status)
        visit = set()
        have_key = set()
        available = set(initialBoxes)
        total = 0 

        def dfs(box):
            if box in visit or (status[box] == 0 and box not in have_key):
                return 
            visit.add(box)

            nonlocal total
            total +=candies[box]

            # add keys 

            for key in keys[box]:
                have_key.add(key)
                if key in available :
                    dfs(key)


            for b in containedBoxes[box]:
                available.add(b)
                if status[b] == 1 or b in have_key :
                    dfs(b)

        for box in list(available):
            if status[box] == 1 or box in have_key:
                dfs(box)

        return total

            
        