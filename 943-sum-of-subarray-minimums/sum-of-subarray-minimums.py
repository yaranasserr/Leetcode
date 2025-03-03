class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        Mod = 10 ** 9  +7 
        res = 0 
        stack = [] # index,num

        for i , n in enumerate(arr):
            while stack and n < stack[-1][1]:
                j,m = stack.pop() # index and value top of stack 
                # how many subarrays including j , m as minimum 
                # getting the distance 
                #  j     i 
                #1 2 3 4 1
                left = j - stack[-1][0] if stack else j+1 # index 

                right = i - j 
                res = (res + m *left *right) %Mod 
            stack.append((i,n))

        for i in range(len(stack)):
            j, n = stack[i]
            left = j -stack[i-1][0] if i> 0 else j+1
            right = len(arr) - j 
            res = (res + n *left *right) %Mod 

        return res

            



        return res