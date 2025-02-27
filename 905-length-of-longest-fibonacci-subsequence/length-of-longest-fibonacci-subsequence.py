class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        arr_set = set(arr)
        res = 0 

        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                prev = arr[i]
                cur = arr[j]
                nxt = prev+cur
                length = 2
                while nxt in arr_set:
                    length +=1
                    prev = cur
                    cur = nxt 
                    nxt = prev+cur 
                    res = max(res,length)

        return res
      
        
  