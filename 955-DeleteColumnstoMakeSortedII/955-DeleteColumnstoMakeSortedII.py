# Last updated: 12/21/2025, 12:09:30 PM
1class Solution(object):
2    def minDeletionSize(self, A):
3        def is_sorted(A):
4            return all(A[i] <= A[i+1] for i in range(len(A) - 1))
5
6        ans = 0
7        # cur : all rows we have written
8        # For example, with A = ["abc","def","ghi"] we might have
9        # cur = ["ab", "de", "gh"].
10        cur = [""] * len(A)  
11
12        for col in zip(*A):
13            # cur2 : What we potentially can write, including the
14            #        newest column 'col'.
15            # Eg. if cur = ["ab","de","gh"] and col = ("c","f","i"),
16            # then cur2 = ["abc","def","ghi"].
17            cur2 = cur[:]
18            for i, letter in enumerate(col):
19                cur2[i] = cur2[i] + letter
20
21            if is_sorted(cur2):
22                cur = cur2
23            else:
24                ans += 1
25
26        return ans