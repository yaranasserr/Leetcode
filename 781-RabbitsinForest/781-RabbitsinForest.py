# Last updated: 4/20/2025, 3:16:37 PM
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        cnts = Counter(answers)
        total_rabbits = 0 
        for k , cnt in cnts.items():
            groups = math.ceil(cnt / (k + 1))
            total_rabbits += groups * (k + 1)

        return total_rabbits

        