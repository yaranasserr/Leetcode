class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1 or (pow(3,20)) % n != 0:
            return False
            
	
        else:
            return True
	
        