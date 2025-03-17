class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq  ={}
        for i in nums :
            if i in freq :
                freq[i] +=1
            else:
                freq[i] = 1

        for val in freq.values():
            if val%2 != 0 :
                return False

        return True 

        