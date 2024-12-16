class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_length = 0
        start = 0
        visited = {}

        for i, char in enumerate(s):
            if char in visited and visited[char] >= start:
                start = visited[char] + 1
            visited[char] = i
            max_length = max(max_length, i - start + 1)

        return max_length




        
        