# Last updated: 7/23/2025, 3:10:05 PM
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        # Helper to check if a string is a palindrome
        def is_palindrome(word):
            return word == word[::-1]

        # Backtracking function
        def backtrack(start, path):
            # If we reach the end of the string, save the path
            if start == len(s):
                result.append(path[:])
                return

            # Try every possible end index
            for end in range(start + 1, len(s) + 1):
                current = s[start:end]
                if is_palindrome(current):
                    path.append(current)        # Choose
                    backtrack(end, path)        # Explore
                    path.pop()                  # Un-choose (backtrack)

        backtrack(0, [])
        return result
