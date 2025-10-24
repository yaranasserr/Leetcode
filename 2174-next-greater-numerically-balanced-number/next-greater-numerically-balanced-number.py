

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        for i in range(n + 1, 1224445):
            nums = list(map(int, str(i)))
            if all(k == v for k, v in Counter(nums).items()):
                return i
