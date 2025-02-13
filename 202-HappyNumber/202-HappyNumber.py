class Solution:
    def isHappy(self, n: int) -> bool:
        #int(digit) for digit in str(num)
        hashmap={}
        res = 0
        def op(num):
            op = sum((int(digit))**2 for digit in str(num))
            return op 

        
        while n!= 1 and n not in hashmap :
            next_val = op(n)
            hashmap[n] = next_val
            n=next_val

        return n == 1
