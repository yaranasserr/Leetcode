# Last updated: 8/14/2025, 5:52:57 PM
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        same = ["999","888","777","666","555","444","333","222","111","000"]
        for n in same:
            if n in num:
                return n
        return ""
