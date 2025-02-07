class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_color = {}  # Maps each ball to its current color
        color_set = {}   # Maps each color to the set of balls with that color
        result = []
        
        for ball, color in queries:
            # If the ball was already colored, remove it from its previous color set
            if ball in ball_color:
                prev_color = ball_color[ball]
                color_set[prev_color].remove(ball)
                if not color_set[prev_color]:  # Remove the color if no balls remain
                    del color_set[prev_color]

            # Assign the new color to the ball
            ball_color[ball] = color
            if color not in color_set:
                color_set[color] = set()
            color_set[color].add(ball)

            # Store the count of distinct colors
            result.append(len(color_set))

        return result
        
        # mapping = {i:[] for i in range(limit+1)}
        # colors = {j:[] for j in range(limit+1)}
        # for i , c in queries:
        #     mapping[i].append(c)
        #     colors[i].append(len(set(val for sublist in mapping.values() for val in sublist)))

        # return colors.values()

    #{0: [], 1: [4, 3], 2: [5], 3: [4], 4: []}

    #Return an array result of length n, where result[i] denotes the number of distinct colors after ith query.
    # 1st query : 1 balls: 1
    # 2nd query : 2  balls  :1 , 2
    # 3rd query : 2 balls : ball 1 , 2
    # 4th : ball 1 2 3 
