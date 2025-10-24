# Last updated: 10/24/2025, 12:30:28 PM


# class Solution:
#     def nextBeautifulNumber(self, n: int) -> int:
#         for i in range(n + 1, 1224445):
#             nums = list(map(int, str(i)))
#             if all(k == v for k, v in Counter(nums).items()):
#                 return i
from collections import Counter
class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        return next(i for i in range(n + 1, 1224445) if all(k == v for k, v in Counter(map(int, str(i))).items()))
