class Solution:
    def numberOfSubstrings(self, s: str) -> int: 
        l = 0 
        count = [0]*3 
        res = 0 
        for r in range(len(s)):
            count[ord(s[r])-ord("a")] +=1
            while count[0] and count[1] and count[2]:
                res+= len(s) - r 
                count[ord(s[l])-ord("a")] -=1
                l+=1
        return res


        # brute force 
        # # slice the substring to have min 3 characters 
        # # count how many sub string have count of a , b , c >= 1 
        # # two for loops 
        # res = []
        # for i in range(len(s)) :
        #     for j in range(i+1,len(s)+1):
        #         if len(s[i:j]) >=3:
        #             res.append(s[i:j])

        # def freq(w):
        #     freq={}
        #     for i in w :
        #         freq[i] = 1+freq.get(i,0)
        #     return  freq 

        # def contains_abc(word):
        #     frequencies = freq(word)
        #     return all(frequencies.get(char, 0) >= 1 for char in 'abc')

        # count = 0 

        # for w in res :
        #     if contains_abc(w):
        #         count +=1 

        # return count




        

        




        