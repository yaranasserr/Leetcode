# Last updated: 3/25/2025, 4:36:27 PM
class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        x = []
        y=[]

        for x1,y1,x2,y2 in rectangles :
            x.append((x1,x2))
            y.append((y1,y2))


        x.sort()
        y.sort()

        def count_nonoverlappingintervals(interval):
            count = 0 
            prevend = - 1

            for start , end in interval:
                if prevend <= start :
                    count +=1 
                prevend = max(end,prevend)


            return count 




        return max(count_nonoverlappingintervals(x),count_nonoverlappingintervals(y))>= 3 


        # def count_nonoverlappingintervals(interval):
        #     interval.sort(key=lambda x:x[0])
        #     prevend = interval[0][1]

        #     count = 1
        #     for start , end in interval[1:]:
        #         if start >= prevend :
        #             count +=1 

        #     return count 

        # # non overlapping intervals 

        # if count_nonoverlappingintervals(xintervals) >= 3 or count_nonoverlappingintervals(yintervals) >= 3 : 

        #     return True 

        # return False 

        
        