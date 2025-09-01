# Last updated: 9/1/2025, 3:47:56 PM
import heapq

class Solution:
    def maxAverageRatio(self, classes: list[list[int]], extraStudents: int) -> float:
        # build heap with negative gain
        pq = [(-( (p+1)/(t+1) - p/t ), p, t) for p, t in classes]
        heapq.heapify(pq)

        # distribute students
        for _ in range(extraStudents):
            gain, p, t = heapq.heappop(pq)
            p, t = p+1, t+1
            new_gain = (p+1)/(t+1) - p/t
            heapq.heappush(pq, (-new_gain, p, t))

        # calculate average
        return sum(p/t for _, p, t in pq) / len(classes)
