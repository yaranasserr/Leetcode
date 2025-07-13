from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None  

        q = deque([root])  

        while q:
            prev = None  # Reset previous node for each level

            for _ in range(len(q)):  
                node = q.popleft()  

                if prev:
                    prev.next = node  # Connect previous node's next to current node
                prev = node  # Update previous node

                if node.left:
                    q.append(node.left) 
                if node.right:
                    q.append(node.right)  

        return root  
