class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res = []
        n = len(potions)

        def binary_search(a):
            l , r = 0, n-1
            while l<=r :
                mid = (l+r)//2
                if a*potions[mid]>= success:
                    r = mid-1
                else:
                    l = mid+1

            return l # first valid potion

        for s in spells:
            idx = binary_search(s)
            res.append(n-idx)

        return res 


        