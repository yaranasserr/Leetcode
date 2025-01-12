# class Solution:
#     def canBeValid(self, s: str, locked: str) -> bool:
#         # O(n) time and space 
#         stack_locked = []
#         stack_unlocked = []
#         # matching closing para (

#         for i in range(len(s)):
#             if locked[i] == "0":
#                 stack_unlocked.append(i)
#             elif s[i] == "(":
#                 stack_locked.append(i)
#             # closing
#             else:
#                 if stack_locked:
#                     stack_locked.pop()
#                 elif stack_unlocked :
#                     stack_unlocked.pop()
#                 else :
#                     return False 
#         while stack_locked and stack_unlocked[-1] < stack_locked[-1]:
#             stack_locked.pop()
#             stack_unlocked.pop()

#         if stack_locked:
#             return False

#         return True  if len(stack_unlocked) % 2 == 0 else False 




class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        # Quick check: If length of s is odd, it can't be valid
        if len(s) % 2 != 0:
            return False
        
        # Forward pass: Check if we can balance as we move left to right
        open_count = 0  # Count of usable '('
        unlock_count = 0  # Count of unlockable positions
        for i in range(len(s)):
            if locked[i] == "0":
                unlock_count += 1
            elif s[i] == "(":
                open_count += 1
            else:  # s[i] == ")"
                if open_count > 0:
                    open_count -= 1
                elif unlock_count > 0:
                    unlock_count -= 1
                else:
                    return False  # No way to balance
            
        # Backward pass: Check if we can balance as we move right to left
        close_count = 0  # Count of usable ')'
        unlock_count = 0  # Reset unlockable count
        for i in range(len(s) - 1, -1, -1):
            if locked[i] == "0":
                unlock_count += 1
            elif s[i] == ")":
                close_count += 1
            else:  # s[i] == "("
                if close_count > 0:
                    close_count -= 1
                elif unlock_count > 0:
                    unlock_count -= 1
                else:
                    return False  # No way to balance

        return True





        