class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        y=0
        
     
        for i in range(1,len(prices)):
             if(prices[i]>prices[i-1]):
                     x=prices[i]-prices[i-1]
                     y=y+x 
        return y
          
                            
           
                        
                          
                            
                        
                
            
        #for i in prices:
            # if(prices[0]>= prices[i]):
            
                   # return 0
        
          
                
                    
                           
                    
                 
                     
            
               
        
                    
            
                    
                
                
        
            
        