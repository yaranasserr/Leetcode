# Last updated: 5/13/2025, 5:51:27 PM
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        # letters = {char:[] for char in list("abcdefghijklmnopqrstuvwxyz")}
        # freq[ord('a') - ord('a')]  # this gives freq[0], which is count of 'a'
        # print(letters)
        freq = [0] *26 
     
        for ch in s :
            freq[ord(ch) - ord('a')]  +=1 

        MOD = 10**9 + 7

        for _ in range(t):
            new_freq = [0] * 26
            for i in range(25):  # 'a' to 'y'
                new_freq[i + 1] = (new_freq[i + 1] + freq[i]) % MOD
            # handle 'z'
            new_freq[0] = (new_freq[0] + freq[25]) % MOD  # 'a'
            new_freq[1] = (new_freq[1] + freq[25]) % MOD  # 'b'
            freq = new_freq


        result = sum(freq) % MOD

        return result


     

        