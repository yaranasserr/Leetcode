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
        if not root:
            return None 
        
    
        q=collections.deque()
        q.append(root)
        while q:
            qlen=len(q)
            prev = None

            for i in range(qlen):
                node=q.popleft()
                # connect the pervious node to the current node 
                if prev:
                    prev.next = node 
                prev = node 
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if prev:
                prev.next=None
                    
        return root

       


        