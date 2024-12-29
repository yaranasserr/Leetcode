class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev = None
        minimum_distance = float('inf')

        # Helper function for in-order traversal
        def dfs(node):
            nonlocal prev, minimum_distance
            if not node:
                return
            # Traverse the left subtree
            dfs(node.left)
            # Calculate the minimum difference
            if prev is not None:
                minimum_distance = min(minimum_distance, abs(node.val - prev))
            # Update prev to the current node's value
            prev = node.val
            # Traverse the right subtree
            dfs(node.right)

        # Perform in-order traversal
        dfs(root)
        return minimum_distance
