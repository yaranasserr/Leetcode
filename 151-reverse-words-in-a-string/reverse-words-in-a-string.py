class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()

        stack = []
        arr =[]
        for w in words :
            stack.append(w)


        while stack :
            arr.append(stack.pop())

        return " ".join(arr)  
        