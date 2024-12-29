class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = []
        products.sort() # n log n
        l,r = 0, len(products)-1

        for i in range(len(searchWord)):
            c= searchWord[i]

            # eleminating that dont have the same prefix
            # ith char not equal to the letter in the word 
            while l<=r and (len(products[l]) <= i or products[l][i]!=c):
                l+=1
            while l<=r and (len(products[r]) <= i or products[r][i]!=c):
                r-=1

            res.append([])
            remain = r - l +1  # size of window , no of words with 
            # if the words are less than 3 
            for j in range(min(3,remain)):
                res[-1].append(products[l+j])

        return res




