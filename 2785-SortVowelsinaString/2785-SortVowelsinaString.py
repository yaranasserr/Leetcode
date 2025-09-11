# Last updated: 9/11/2025, 3:53:04 PM
class Solution:
    def sortVowels(self, s: str) -> str:
        arr = [ch for ch in s if ch in "aeoiuAEOIU" ]

        # for ch in s :
        #     if ch in "aeoiuAEOIU":
        #         arr.append(ch)

        arr.sort()
        s = list(s)
        ch ,i = 0 ,0 
        while ch < len(s) and i < len(arr):
            if s[ch] in "aeoiuAEOIU":
                s[ch] = arr[i]
                i+=1

            ch+=1

        return "".join(s) 

        

        