class Solution:
    def intersect(self, tasks1: List[int], tasks2: List[int]) -> List[int]:
        # ans=[]
        # for i in nums1:
        #     if i in nums2:
        #         ans.append(i)
        #         nums2.remove(i)
        # return ans
        def freq(arr):
            c= {}
            for n in arr:
                if n in c:
                    c[n] += 1
                else:
                    c[n] = 1
            return c
            # for n in arr :
            #     c[n] = 1+c.get(n,0)
            # return c

        res = []
        c1 = freq(tasks1)
        c2= freq(tasks2)

        for num in c1 :
            if num in c2 :
                res += [num] * min(c1[num],c2[num])
        return res