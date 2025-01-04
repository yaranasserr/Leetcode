class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = set()  # (mid_c , outer_c)
        # set on the lft , hash map on the right 
        left = set()
        right=Counter(s)

        for m in s:
            # remove it from the right
            right[m] -=1 
            for c in left :
                if right[c] >0:
                    res.add((m,c))

            left.add(m)

        
        return len(res)







        