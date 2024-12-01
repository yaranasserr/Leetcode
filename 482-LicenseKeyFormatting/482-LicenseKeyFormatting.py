class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        result = ""
        s = s.replace("-","").upper()
        len_s = len(s)
        
        remainder = len_s % k 
        
        if remainder != 0 :
            result = s[0:remainder] + "-"
            
        for i in range(remainder ,len_s, k):
            result = result + s[i:i+k] + "-"

        return result[:-1]
