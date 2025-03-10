class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # convert nums to strings 
        nums = list(map(str,nums))
        
        def compare(a,b):
            if a+b > b+a :
                return -1 # a should be before b 
            else :
                return 1 

        nums.sort(key=cmp_to_key(compare))

        result ="".join(nums)
        return '0' if result[0] == '0' else result

        