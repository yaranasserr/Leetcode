class ProductOfNumbers:
    def __init__(self):
        self.prefix = [1]  # Prefix product list (1 to handle division properly)
        
    def add(self, num: int) -> None:
        if num == 0:
            self.prefix = [1]  # Reset if 0 is added
        else:
            self.prefix.append(self.prefix[-1] * num) 
            
    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix):  
            return 0
        return self.prefix[-1] // self.prefix[-(k+1)]  


        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)