# Last updated: 7/13/2025, 4:58:26 PM
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root :return None

        q=deque([root])
      

        while q :
            prev = None
           
            for i in range(len(q)):
                node = q.popleft()
                if prev :
                    prev.next = node 
                prev = node 
                if node.left :
                    q.append(node.left)
                if node.right:

                    q.append(node.right)

            if prev :
                prev.next = None

           

        return root 

                
        