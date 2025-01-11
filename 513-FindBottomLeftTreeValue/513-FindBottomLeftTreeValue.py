class Solution(object):
    def findBottomLeftValue(self, root):
        if not root:
            return None
        
        queue = deque([root])
        leftmost_val = None
        
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                if i == 0:  # First node of the level, update leftmost value
                    leftmost_val = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return leftmost_val