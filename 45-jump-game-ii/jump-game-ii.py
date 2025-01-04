class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        
        # BFS Initialization
        queue = deque([(0, nums[0])])  # store (index, jump_value)
        visited = [False] * n
        visited[0] = True
        jumps = 0

        while queue:
            level_size = len(queue)
            jumps += 1
            
            for _ in range(level_size):
                idx, val = queue.popleft()

                # Check all possible next jumps
                for i in range(1, val + 1):
                    next_idx = idx + i
                    if next_idx < n and not visited[next_idx]:
                        visited[next_idx] = True
                        queue.append((next_idx, nums[next_idx]))
                        
                        if next_idx == n - 1:  # Reached the last index
                            return jumps

        