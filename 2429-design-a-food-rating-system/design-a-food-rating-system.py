class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
       
        self.fooddict = {} # food (key) :[ cusine,ratning]
        self.cusinedict={} # cusine : food ( use max heapq to put them in max order with respect to rating)

        for f,c,r in zip(foods,cuisines,ratings):
            self.fooddict[f] = [c,r]
            if c not in self.cusinedict:
                self.cusinedict[c] = []
            heapq.heappush(self.cusinedict[c], (-r, f))
        
    def changeRating(self, food: str, newRating: int) -> None:
        c,_ = self.fooddict[food]
        self.fooddict[food][1] = newRating
        heapq.heappush(self.cusinedict[c], (-newRating, food))

        

    def highestRated(self, cuisine: str) -> str:
        heap = self.cusinedict[cuisine]
        while heap :
            rating , food = heap[0]
            if self.fooddict[food][1] == - rating :
                return food 
            else:
                heapq.heappop(heap)
        # return heap[0][1]   # ( -rating, food ) → take food
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)