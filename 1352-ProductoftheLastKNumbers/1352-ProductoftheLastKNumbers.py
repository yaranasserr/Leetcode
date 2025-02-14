class ProductOfNumbers:

    def __init__(self):
        self.prefix = [1]  # Prefix product list (1 to handle division)
        
    def add(self, num: int) -> None:
        if num == 0:
            self.prefix = [1]  # Reset prefix product list if 0 is added
        else:
            self.prefix.append(self.prefix[-1] * num)  # Store cumulative product
            
    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix):  # If k is larger than available elements, return 0
            return 0
        return self.prefix[-1] // self.prefix[-(k+1)]  # Compute product in O(1)

# class ProductOfNumbers:

#     def __init__(self):
#         self.res = []  # Stores added numbers
        
#     def add(self, num: int) -> None:
#         self.res.append(num)  # Append number to the list
        
#     def getProduct(self, k: int) -> int:
#         if k > len(self.res):  # Ensure k does not exceed available numbers
#             return 0
        
#         p = 1
#         for i in range(len(self.res) - 1, len(self.res) - 1 - k, -1):
#             if self.res[i] == 0:  # If zero is encountered, return 0
#                 return 0
#             p *= self.res[i]

#         return p
