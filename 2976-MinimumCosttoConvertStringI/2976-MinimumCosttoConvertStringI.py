# Last updated: 1/29/2026, 12:21:43 PM
1class Solution:
2    def minimumCost(
3        self,
4        source: str,
5        target: str,
6        original: List[str],
7        changed: List[str],
8        cost: List[int],
9    ) -> int:
10        # Create a graph representation of character conversions
11        adjacency_list = [[] for _ in range(26)]
12
13        # Populate the adjacency list with character conversions
14        conversion_count = len(original)
15        for i in range(conversion_count):
16            adjacency_list[ord(original[i]) - ord("a")].append(
17                (ord(changed[i]) - ord("a"), cost[i])
18            )
19
20        # Calculate shortest paths for all possible character conversions
21        min_conversion_costs = [
22            self._dijkstra(i, adjacency_list) for i in range(26)
23        ]
24
25        # Calculate the total cost of converting source to target
26        total_cost = 0
27        for s, t in zip(source, target):
28            if s != t:
29                char_conversion_cost = min_conversion_costs[ord(s) - ord("a")][
30                    ord(t) - ord("a")
31                ]
32                if char_conversion_cost == float("inf"):
33                    return -1  # Conversion not possible
34                total_cost += char_conversion_cost
35
36        return total_cost
37
38    def _dijkstra(
39        self, start_char: int, adjacency_list: List[List[tuple]]
40    ) -> List[int]:
41        # Priority queue to store characters with their conversion cost, sorted by cost
42        priority_queue = [(0, start_char)]
43
44        # List to store the minimum conversion cost to each character
45        min_costs = [float("inf")] * 26
46
47        while priority_queue:
48            current_cost, current_char = heapq.heappop(priority_queue)
49
50            if min_costs[current_char] != float("inf"):
51                continue
52
53            min_costs[current_char] = current_cost
54
55            # Explore all possible conversions from the current character
56            for target_char, conversion_cost in adjacency_list[current_char]:
57                new_total_cost = current_cost + conversion_cost
58
59                # If we found a cheaper conversion, update its cost
60                if min_costs[target_char] == float("inf"):
61                    heapq.heappush(
62                        priority_queue, (new_total_cost, target_char)
63                    )
64
65        # Return the list of minimum conversion costs from the starting character to all others
66        return min_costs