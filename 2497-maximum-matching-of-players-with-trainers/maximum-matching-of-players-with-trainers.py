class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        matching = 0 
        i = 0 
        j = 0 
        while i < len(players) and j < len(trainers):
            if trainers[j] < players[i]:
                j +=1 

            else:
                matching +=1 
                i+=1
                j+=1

        return matching

        
        