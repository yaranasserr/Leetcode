class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k :
            return False

        freq = Counter(s)
        odd_count = 0 
        for val in freq.values():
            if val % 2 != 0 :
                odd_count+=1 

        if odd_count > k :
            return False

        else:
            return True 



