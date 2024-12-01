class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]

        for i in range(rowIndex):
            next_row = [0]* (len(res)+1)
            # iretate in every value in the pervious row
            for j in range(len(res)):
                next_row[j] += res[j]
                next_row[j+1] += res[j]
            res = next_row

        return res 





        # rows = pascal(34)



        # def pascal(self,rows):
        #     res = [[1]]

        #     for i in range(rows-1):
        #         temp = [0] + res[-1] +[0]
        #         row =[] # the new row 
        #         for j in range(len(res[-1])+1): # pervious row
        #             row.append(temp[j] + temp[j+1])
        #         res.append(row)

        #     return res 



        
        