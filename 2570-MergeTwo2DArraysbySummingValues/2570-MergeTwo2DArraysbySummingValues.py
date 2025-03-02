class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        one ={}
        two = {}
        def tohash(nums,dic):
            for i in range(len(nums)):
                index = nums[i][0]
                val = nums[i][1]
                dic[index] = val

            return dic 

        tohash(nums1,one)
        tohash(nums2,two)

        res = {}

        for key in one:
            if key in two:
                res[key] = one[key] + two[key]
            elif key not in two :
                res[key] = one[key]
        for key in two :
            if key not in one :
                res[key] = two[key]
    
        sorted_res = dict(sorted(res.items()))
    
        res_list = list(sorted_res.items())
        return res_list
            

                    


            
        