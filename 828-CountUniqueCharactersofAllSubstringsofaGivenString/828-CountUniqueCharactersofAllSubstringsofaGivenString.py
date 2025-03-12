class Solution(object):
    def uniqueLetterString(self, s):
        """
        :type s: str
        :rtype: int
        """
        cur = res = 0 
        post_dict = collections.defaultdict(lambda:[-1,-1])

        for i , char in enumerate(s):
            cur +=(i - post_dict[char][0]-(post_dict[char][0]-post_dict[char][1]))

            post_dict[char][1] = post_dict[char][0]
            post_dict[char][0]= i 

            res+=cur 

        return res 
        