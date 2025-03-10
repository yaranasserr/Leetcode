class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
            s = list(s)
            n = len(s)
            moves = 0

            left, right = 0, n - 1

            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    l = right
                    while l > left and s[l] != s[left]:
                        l -= 1

                    if l == left:  # No matching character found, so this char must go to the center
                        s[left], s[left + 1] = s[left + 1], s[left]
                        moves += 1
                    else:
                        for k in range(l, right):
                            s[k], s[k + 1] = s[k + 1], s[k]
                            moves += 1
                        left += 1
                        right -= 1

            return moves

        



# palindrome

#         res = 0

#         for i in range(len(s)):
#             # odd length
#             l=r=i

#             while l >= 0 and r < len(s) and s[l]==s[r]:
#                 res +=1 
#                 l -= 1
#                 r+=1

#             l,r=i,i+1

#             while l >= 0 and r < len(s) and s[l]==s[r]:
#                 res +=1 
#                 l -= 1
#                 r+=1

#         return res





        