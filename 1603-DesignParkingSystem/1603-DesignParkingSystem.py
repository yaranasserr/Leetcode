class ParkingSystem(object):

    def __init__(self, big, medium, small):
        self.big = big
        self.medium = medium
        self.small = small
        

    def addCar(self, carType):
        if carType ==1 and self.big >0:
            self.big -=1 
            return True 
  

        if carType == 2 and self.medium > 0 :
            self.medium -=1 
            return True 
     
        if carType == 3 and self.small > 0 :
            self.small -=1
            return True 
            
        return False 

    
        

    # def addCar(self, carType):
    #     """
    #     :type carType: int
    #     :rtype: bool
    #     """
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)