class stringmod():
    def __init__(self,word):
        self.word = word 

    def __lt__(self,other):
        return self.word>other.word
class SORTracker(object):

    def __init__(self):
        self.left = [] 
        self.right = [] #max-heap: stores the top k best locations
        

    def add(self, name, score):
        """
        :type name: str
        :type score: int
        :rtype: None
        """
        if not self.left :
            heapq.heappush(self.right,[-score,name])
        elif self.left[0][0] < score or (self.left[0][0] == score  and self.left[0][1].word>name):
            #when the current comes before ie higher score or lexiographically smaller name 
            heapq.heappush(self.left , [score,stringmod(name)])
            scorenew , obj = heapq.heappop(self.left)
            namenew = obj.word
            heapq.heappush(self.right,[-scorenew,namenew])

        else:
            heapq.heappush(self.right,[-score,name])


        # heapq.heappush(self.left,(-score,name)) # maxheap
        # if len(self.left)> self.k+1 :
        #     best = heapq.heappop(self.left)
        #     heapq.heappush(self.right,(-best[0],-best[1]))
        

    def get(self):
        """
        :rtype: str
        """
        # self.k +=1

        # return  self.left[0][1]
        score,name = heapq.heappop(self.right)
        heapq.heappush(self.left, [-score,stringmod(name)])
        return name 
        


# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()