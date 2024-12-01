class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        new_s = ""
        new_t = ""
        for i in range(len(s)):
                if s[i]=="#":
                    new_s= new_s[:-1]
                else:
                    new_s = new_s + s[i]

                
        for i in range(len(t)):
                if t[i]=="#":
                    new_t =new_t[:-1]
                else:
                    new_t = new_t + t[i]

                
        return new_s == new_t