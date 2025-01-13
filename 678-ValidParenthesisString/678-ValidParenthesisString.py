class Solution:
    def checkValidString(self, s: str) -> bool:
        left_stack = []  # Stack to store indices of '('
        star_stack = []  # Stack to store indices of '*'
        
        for i, char in enumerate(s):
            if char == '(':
                left_stack.append(i)
            elif char == '*':
                star_stack.append(i)
            else:  # char == ')'
                if left_stack:  # Try to match with a '('
                    left_stack.pop()
                elif star_stack:  # Try to match with a '*'
                    star_stack.pop()
                else:
                    return False  # If there's no matching '(' or '*', it's invalid

        # Now match the remaining '(' with '*'
        while left_stack and star_stack:
            # if the most recent unmatched '(' appears after the most recent '*' in the string.

            if left_stack[-1] > star_stack[-1]:
                return False
            left_stack.pop()
            star_stack.pop()

        return not left_stack  # If left_stack is empty, all '(' were matched
