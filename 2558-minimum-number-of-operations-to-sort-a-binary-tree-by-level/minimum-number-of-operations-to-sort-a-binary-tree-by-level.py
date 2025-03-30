# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0  # No swaps needed for an empty tree

        ops = 0
        q = deque([root])

        while q:
            level = []
            for _ in range(len(q)):  # Process current level
                node = q.popleft()
                if node:
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

            if level:  # Only process non-empty levels
                sorted_level = sorted(level)  # Sorted copy
                sorted_indices = {num: i for i, num in enumerate(sorted_level)}  
                unsorted = {i: num for i, num in enumerate(level)}  
                
                visited = set()
                
                def dfs(i):
                    cycle = set()
                    while i not in visited:
                        visited.add(i)
                        cycle.add(i)
                        val = unsorted[i]  # Get value at current index
                        i = sorted_indices[val]  # Move to sorted index
                    return len(cycle) - 1  # Swaps needed for this cycle

                swaps = 0
                for i in range(len(level)):
                    if i not in visited:
                        swaps += dfs(i)

                ops += swaps  # Accumulate swaps across levels

        return ops







                        
                    # sortedlevel=level.sort()
                    # sorted_indices={i:num for i,num in enumerate(sorted_level)}
                    # unsorted ={i:num for i,num in enumerate(level)}
                    # # identify cycle
                    # cycle = set()
                    # # swaps = len(cycle)-1 = dfs(0)[1] -1 
                    # def dfs(i):
                    #     if i in cycle :
                    #         return True and len(cycle)

                    #     # sorted = {5:0,6:1,7:2,8:3}
                    #     # unsorted = {7:0 , 6:1,8:2,5:3}
                    #     #7 (index 0) → 7 belongs at index 2
                    #     # 8 (index 2) → 8 belongs at index 3
                    #     # 5 (index 3) → 5 belongs at index 0
                    #     # This forms a cycle (0 → 2 → 3 → 0), requiring 3 - 1 = 2 swaps.
                    #     # 6 (index 1) → 6 is already in place.
                    #     for i in unsorted[i]:
                    #         cycle.add(i) # added 0 to cycle from unsorted[0]
                    #         # check in sorted the value of this i and add its index
                    #         val = unsorted[i].val()
                    #         cycle.add(sorted_indices[val).key())

                    










"""
Find the sorted order.

Track original indices.

Identify cycles in the permutation.

Each cycle of length  \U0001d458


k−1 swaps.

Sum over all cycles to get the minimum swaps.
"""
                    

              
      


"""
Amazon Alexa Music Recommendation -
The Amazon Alexa team is working on improving its music recommendation system. The system represents user song preferences as a binary tree, where each node contains a unique song ID. However, the songs at each level of the tree are not in a proper manner so that we can recommend them to the user.

Your task is to determine the minimum number of swaps required to sort the song IDs at each level in ascending order. You need to return the total number of swaps required for the entire tree.

Example:
5
/ \
8 3
/ \ / \
10 2 7 6

Levels and Swaps Needed:

Level 0: [5] (Already sorted, swaps = 0)
Level 1: [3, 8] (not sorted, swaps = 1)
Level 2: [10, 2, 7, 6] → not Sorted (Swaps = 2)"""
        