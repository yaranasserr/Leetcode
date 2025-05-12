class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = set()
        n = len(digits)

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i!= j and j!=k and i!=k :
                        a,b,c= digits[i] , digits[j] , digits[k]
                        if a!= 0 and c%2 == 0 :
                            num = a*100 + b *10 +c 
                            res.add(num)

        return sorted(res)

        # allnums = range(100,1000)
        # all_evens =[x for x in allnums if x % 2== 0]
        # res = []
        # if any digits in all_evens:
        #     res.append(i)
        