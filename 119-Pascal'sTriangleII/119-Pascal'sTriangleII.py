class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = []
        
        for i in range(1,rowIndex+2):
            temp = [0] * i
            temp[0], temp[-1] = 1 ,1
            
            if len(temp) > 2 :
                for j in range(1,i-1):
                    temp[j] = result[i-2][j-1] + result[i-2][j]
                result.append(temp)
            else:
                result.append(temp)
                
        return result[rowIndex]
                
        
        