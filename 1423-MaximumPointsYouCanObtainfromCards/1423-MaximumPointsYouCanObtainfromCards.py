# Last updated: 3/27/2025, 3:36:42 AM
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total_pts = sum(cardPoints)
        
        #remove a sub-array from cardPoints with length n - k.
        #max(answer, total_pts - sumOfCurrentWindow)
        l = 0
        n = len(cardPoints)
        sumwindow =  sum(cardPoints[:(n-k)])
        minimum = sumwindow  
      
    
        for r in range(n-k,n):
            sumwindow = sumwindow - cardPoints[l] + cardPoints[r]
           
            minimum= min(minimum,sumwindow )
            
            l+=1

        return total_pts - minimum

        






        
      


        