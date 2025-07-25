# Last updated: 7/25/2025, 3:48:54 PM
class Solution:
    def calculate(self, s: str) -> int:
        # op = total sum so far
        # cur = current number being built
        # sign = +1 or -1, used for applying the last seen '+' or '-'
        # stack = stores previous (op, sign) when entering parentheses
        op, cur, sign = 0, 0, 1
        stack = []

        for c in s:
            if c.isdigit():
                # Build the current number
                cur = cur * 10 + int(c)
            
            elif c in "+-":
                # Add previous number with its sign
                op += sign * cur
                cur = 0
                # Update sign based on current operator
                sign = 1 if c == '+' else -1

            elif c == "(":
                # Push current op and sign to stack before a new sub-expression
                stack.append(op)
                stack.append(sign)
                # Reset op and sign for new sub-expression
                op = 0
                sign = 1

            elif c == ")":
                # Add current number before closing
                op += sign * cur
                cur = 0
                # Multiply with sign before parenthesis
                op *= stack.pop()   # sign
                # Add to previous total before parenthesis
                op += stack.pop()   # previous op

        return op + (sign * cur)
