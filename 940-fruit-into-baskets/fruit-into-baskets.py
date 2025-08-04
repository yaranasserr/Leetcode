from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        fruit_count = {}
        maximum = 0

        for r in range(len(fruits)):
            fruit = fruits[r]
            fruit_count[fruit] = fruit_count.get(fruit, 0) + 1

            while len(fruit_count) > 2:
                fruit_count[fruits[l]] -= 1
                if fruit_count[fruits[l]] == 0:
                    del fruit_count[fruits[l]]
                l += 1


            maximum = max(maximum, r - l + 1)

        return maximum
