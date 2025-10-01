# Last updated: 10/1/2025, 12:16:40 PM
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        cons = 0 
        while  numBottles >= numExchange :
            cons += numExchange
            numBottles -=numExchange

            numBottles +=1 # exchange them for one full bottle


        return numBottles + cons
        