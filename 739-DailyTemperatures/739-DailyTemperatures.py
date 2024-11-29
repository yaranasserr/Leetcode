class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        stack=[0]*n
        output=[0]*n
        count=0

        for i in range(n):
            # While the current temperature is greater than the temperature
            # at the index stored at the top of the stack, update the output
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                output[prev_index] = i - prev_index
            stack.append(i)  # Push current index onto the stack
        
        return output