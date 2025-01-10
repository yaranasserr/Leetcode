from collections import Counter 
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        count_2 = defaultdict(int)

        for w in words2:
            count_w=Counter(w)

            for c , cnt in count_w.items():
                count_2[c] = max(count_2[c],cnt)

        res = []
        for w in words1:
            count_w = Counter(w)
            flag = True 
            for c , cnt in count_2.items():
                if count_w[c] <cnt:
                    flag = False
                    break
            if flag :
                res.append(w)

        return res   

        return res

        # freq = []

        # for w in words1:
        #     freq.append(Counter(w))
        # count  = 0 

        # for w in freq:
        #     if words_2 in w.keys():
        #         count +=1 


        