# Last updated: 12/14/2025, 5:03:35 PM
1class Solution:
2    def numberOfWays(self, corridor: str) -> int:
3        # Store 1000000007 in a variable for convenience
4        MOD = 1_000_000_007
5
6        # Cache the result of each sub-problem
7        cache = [[-1] * 3 for _ in range(len(corridor))]
8
9        # Count the number of ways to divide from "index" to the last index
10        # with "seats" number of "S" in the current section
11        def count(index, seats):
12            # If we have reached the end of the corridor, then
13            # the current section is valid only if "seats" is 2
14            if index == len(corridor):
15                return 1 if seats == 2 else 0
16
17            # If we have already computed the result of this sub-problem,
18            # then return the cached result
19            if cache[index][seats] != -1:
20                return cache[index][seats]
21            
22            # If the current section has exactly 2 "S"
23            if seats == 2:
24                # If the current element is "S", then we have to close the
25                # section and start a new section from this index. Next index
26                # will have one "S" in the current section
27                if corridor[index] == "S":
28                    result = count(index + 1, 1)
29                else:
30                    # If the current element is "P", then we have two options
31                    # 1. Close the section and start a new section from this index
32                    # 2. Keep growing the section
33                    result = (count(index + 1, 0) + count(index + 1, 2)) % MOD
34            else:
35                # Keep growing the section. Increment "seats" if present
36                # element is "S"
37                if corridor[index] == "S":
38                    result = count(index + 1, seats + 1)
39                else:
40                    result = count(index + 1, seats)
41            
42            # Memoize the result, and return it
43            cache[index][seats] = result
44            return cache[index][seats]
45        
46        # Call the count function
47        return count(0, 0)