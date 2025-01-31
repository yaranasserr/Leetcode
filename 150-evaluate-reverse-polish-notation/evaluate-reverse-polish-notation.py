class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda b, a: int(b / a)  
        }

        for token in tokens:
            if token not in operators:
                stack.append(int(token)) 
            else:
                a = stack.pop()  # Second operand
                b = stack.pop()  # First operand
                ans = ops[token](b, a) 
                stack.append(ans)  

        return stack[-1]  # Final result
        