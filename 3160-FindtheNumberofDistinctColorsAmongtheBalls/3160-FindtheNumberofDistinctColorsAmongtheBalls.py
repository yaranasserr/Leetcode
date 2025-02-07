class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_color = {}  # Maps each ball to its current color
        color_set = {}   # Maps each color to the set of balls assigned that color
        result = []

        for i, c in queries:
            # If the ball already has a color, remove it from the previous color's set
            if i in ball_color:
                prev_color = ball_color[i]
                color_set[prev_color].remove(i)
                if not color_set[prev_color]:  # Remove color if no balls remain
                    del color_set[prev_color]

            # Assign the new color
            ball_color[i] = c
            if c not in color_set:
                color_set[c] = set()
            color_set[c].add(i)

            # The number of distinct colors is simply the size of color_set
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
