class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1  
            # generating all 8 childern of every bits like  +1 -1
            # 0000 : 1000 9000  0100 0800 0010 0090 0001 0009
        def childern(lock):
            res = []
            for i in range(4):
                digit =str((int(lock[i]) +1) % 10)
                res.append(lock[:i]+digit+ lock[i+1:])
                digit =str((int(lock[i]) -1 +10) % 10)
                res.append(lock[:i]+digit +lock[i+1:])
            return res




        # bfs
        q = deque()
        # value , no of moves
        q.append(["0000",0])
        visit= set(deadends)


        while q:
            lock , turns = q.popleft()
            if lock == target :
                return turns

            for child in childern(lock):
                if child not in visit:
                    visit.add(child)
                    q.append([child,turns+1])
        return -1

        