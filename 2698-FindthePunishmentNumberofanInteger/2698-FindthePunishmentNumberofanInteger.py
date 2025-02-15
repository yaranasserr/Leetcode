class Solution:
    def punishmentNumber(self, n: int) -> int:
        # backtracking recursion 
        # j index we are currently at 
        # cur :cumaltive sum 
        res = 0 

        def partition(i,cur:int , target:int , string:str):
            if i == len(string) and cur == target :
                return True 

            for j in range(i,len(string)):
                string[i:j+1]
                if partition(j+1,cur+int(string[i:j+1]),target,string):
                    return True 

            return False 

        for i in range(1,n+1):
            if partition(0,0,i,str(i*i)):
                res+= i*i

        return res 
        # # op = sum(int(digit) for digit in str(num))
        # # , [int(digit) for digit in str(squared)
        # product = {}
        # res = []
        # for i in range(n + 1):
        #     squared = i * i
        #     product[i] = squared
        
        # def part(i):
        #     # base case 
        #     if i == sum(part):
        #         res.append(squared)

        #     # generate all partitions of i 
        #     # for ex [100:(10,0)(1,0,0)(1,00)]
        #     part = 


        #     return res 


        

        # for i in product.values():
        #     dfs(i)

                