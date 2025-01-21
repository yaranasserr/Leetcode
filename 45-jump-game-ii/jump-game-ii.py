class Solution:
    def jump(self, nums: List[int]) -> int:
        #bfs easier 
        l=0
        r=0 
        # for cuurent window
        res = 0
        while r < len(nums)-1 :
            farthest = 0
            for i in range(l,r+1):
                farthest = max(farthest , i +nums[i])

            l = r+1
            r = farthest 
            res +=1
        return res 

        # n = len(nums)
        # if n <= 1:
        #     return 0
        
        # # BFS Initialization
        # queue = deque([(0, nums[0])])  # store (index, jump_value)
        # visited = [False] * n
        # visited[0] = True
        # jumps = 0

        # while queue:
        #     level_size = len(queue)
        #     jumps += 1
            
        #     for _ in range(level_size):
        #         idx, val = queue.popleft() # store (index, jump_value)

        #         # Check all possible next jumps
        #         for i in range(1, val + 1):
        #             next_idx = idx + i
        #             if next_idx < n and not visited[next_idx]:
        #                 visited[next_idx] = True
        #                 queue.append((next_idx, nums[next_idx]))
                        
        #                 if next_idx == n - 1:  # Reached the last index
        #                     return jumps
# It tracks each index and its corresponding value, exploring all possible jumps from the current index and incrementing the jump count until the last index is reached.

# Time Complexity: O(n), 
        