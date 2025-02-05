class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        i , j = 0 ,0 
        count = 0


        while i < len(s1) and j < len(s2):
            if s1[i] != s2[j]:
                count +=1

            i+=1
            j+=1
        freq1=Counter(s1)
        freq2 = Counter(s2)

        if (count == 0 or count == 2) and (freq1==freq2):
            return True
        else:
            return False

                

        
                




        