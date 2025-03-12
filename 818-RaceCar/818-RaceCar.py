class Solution(object):
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        queue = collections.deque([(0,0,1)])  # position , moves , speed 
        visit = set()
        while queue :
            moves,position,speed = queue.popleft()
            if position == target :
                return moves 

            if (position , speed) in visit :
                continue 

            else:
                visit.add((position,speed))
                queue.append((moves+1,position+speed , speed*2))
                if (position +speed > target and speed >0) or (position +speed < target and speed < 0 ):
                    speed = -1 if speed > 0 else 1

                    queue.append((moves+1,position,speed))


        # position = 0
        # speed = 1
        # res=[]
        # def A(p,s):
        #     p += s
        #     s = s*2  
        #     return p , s

        # def R(s):
        #     if s > 0 :
        #         s= -1
        #     elif s < 0 :
        #         s = 1
        #     return s

        # while position < target :
        #     position,speed = A(position,speed)
        #     res.append("A")
        #     if position > target and speed > 0 or position < target and speed < 0:
        #         speed = R(speed)
        #         res.append("R")
        #         position,speed = A(position,speed)
        #         res.append("A")


        # return len(res)




            
        