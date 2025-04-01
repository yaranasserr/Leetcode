# Last updated: 4/1/2025, 11:35:52 AM
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        cache = [0]*len(questions)

        def backtrack(i):
            if i >= len(questions):
                return 0 
            if cache[i]:
                return cache[i]
        
            # take the question 
            points , brainpower = questions[i]

            # dont take the question 
            cache[i]= max(backtrack(i+1),points+backtrack(i+1+brainpower))
            return cache[i]

        return backtrack(0)

            

        