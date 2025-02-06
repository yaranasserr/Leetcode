from typing import List

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> List[List[int]]:
        product_cnt = defaultdict(int) # n1*n2 -> count
        pair_cnt = defaultdict(int) # n1*n2 -> count of pairs (a,b) 
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                product = nums[i] *nums[j]
                pair_cnt[product]+= product_cnt[product]
                product_cnt[product]+=1

        res = 0 
        for cnt in pair_cnt.values():
            res+= 8*cnt

        return res


        # perms = [[]]
        # valid_perms = []  # Store valid permutations
        
        # for n in nums:
        #     new_perms = []
        #     for p in perms:
        #         for i in range(len(p) + 1):
        #             p_copy = p.copy()
        #             p_copy.insert(i, n)  # Insert n in every possible position
        #             new_perms.append(p_copy)

        #             # Check if permutation length is 4 and satisfies the condition
        #             if len(p_copy) == 4:
        #                 a, b, c, d = p_copy
        #                 if a * b == c * d:
        #                     valid_perms.append(p_copy)
                            
        #     perms = new_perms
        
        # return len(valid_perms)

