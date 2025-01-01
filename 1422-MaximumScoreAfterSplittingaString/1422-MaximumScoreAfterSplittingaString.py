class Solution:
    def maxScore(self, s: str) -> int:
    

        max_score = 0
       
        total_ones = s.count('1')
   
        left_zeros = 0
        left_ones = 0

       
        for i in range(len(s) - 1):
       
            if s[i] == '0':
                left_zeros += 1
            else:
                left_ones += 1
            
      
            right_ones = total_ones - left_ones
            score = left_zeros + right_ones
            max_score = max(max_score, score)

        return max_score

                


        