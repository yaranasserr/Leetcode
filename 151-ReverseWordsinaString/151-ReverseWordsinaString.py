class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split()
        stack=[]
        for i in words:
            stack.append(i)

        rev=[]

        while stack:
            rev.append(stack.pop())

        return ' '.join(rev)

