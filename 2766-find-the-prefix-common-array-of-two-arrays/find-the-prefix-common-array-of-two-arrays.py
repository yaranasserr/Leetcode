class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:

        n = len(A)
        freq = [0] * (n + 1)
        common_set = set()
        result = []
        
        for i in range(n):
            # Update frequency for the current elements
            #A[0]= 1 B[0] = 3 
           
            freq[A[i]] += 1
            freq[B[i]] += 1
            # freq = [0, 1, 0, 1, 0]
            # Check if they have occurred twice
            if freq[A[i]] == 2:
                common_set.add(A[i])
            if freq[B[i]] == 2:
                common_set.add(B[i])
            
            # Append the size of the common set
            result.append(len(common_set))
        
        return result
        