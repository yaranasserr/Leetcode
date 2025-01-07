class Solution:
    def shortestPalindrome(self, s: str) -> str:
        prefix , suffix = 0,0 
        base = 29
        last_index = 0
        power = 1

        for i,c in enumerate(s):
            char = (ord(c) - ord('a')+1) # a :0  z:25 
            prefix = (prefix*base)
            prefix = (prefix+char)

            suffix = (suffix +char*power)
            power = (power*base)

            if prefix == suffix :
                
                last_index = i 


        suffix = s[last_index +1:]
        return suffix[::-1] +s
        