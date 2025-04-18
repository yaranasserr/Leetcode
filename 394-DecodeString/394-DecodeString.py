class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for i in range(len(s)) :
            if s[i] != "]":

                stack.append(s[i])

            else:
                substr=''
                while stack[-1] != '[' :
                    substr = stack.pop() + substr 
                stack.pop() # pop [

                # get the integar 
                k=''

                while stack and stack[-1].isdigit():
                    # pop the digit
                    k= stack.pop() + k 

                stack.append(int(k) * substr)

        return "".join(stack)


        