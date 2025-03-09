class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # SLIDING WINDOW
        # COUNT THE NUMBER OF WHITES IN A WINDOW OF SIZE K
        l = 0 
        recolor = 0 
        res = k # max num of ops 

        for r in range(len(blocks)):
            if blocks[r] == 'W':
                recolor +=1
            if r - l +1 == k : 
                res = min(res,recolor)
                # length of window is k so increment l 
                if blocks[l] =='W':
                    recolor -=1
                l+=1

        return res 



