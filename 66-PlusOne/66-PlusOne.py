class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s=""
        for i in digits:
            s = s + str(i)
            
            
        number = int(s)
        number = number + 1
        
        result = []
        
        for c in str(number):
            result.append(int(c))
            
        return result
        
            