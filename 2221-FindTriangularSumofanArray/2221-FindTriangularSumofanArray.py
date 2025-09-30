# Last updated: 9/30/2025, 11:38:25 AM
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
            # for i in range( numRows-1):
            # temp = [0] + res[-1] +[0]
            # row =[] # the new row 
            # for j in range(len(res[-1])+1): # pervious row
            #     row.append(temp[j] + temp[j+1])
            # res.append(row)
        temp = nums
        n = len(temp)
        while n !=1 :
        
            for i in range(1,len(temp)):
                
                temp[i-1]= (temp[i-1]+temp[i])% 10
            temp = temp[:-1]
            n = len(temp)

        return temp[0]

      




            

        