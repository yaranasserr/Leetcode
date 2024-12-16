
class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
                    "I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000,
                }
    #largest to smallest add , smallest to largest subtract
    #small no first
    #  4 = 5-1 = IV
    # 9 = 10 -1 = IX
        res =0 
        for i in range(len(s)):
            if i+1 < len(s) and values[s[i]] < values[s[i+1]]:
                res-=values[s[i]]
            else:
                res+=values[s[i]]
        return res 
 