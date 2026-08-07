# Last updated: 8/7/2026, 8:07:21 PM
1class Solution:
2    def smallestNumber(self, num: str, t: int) -> str:
3        temp = t
4        for i in range(2, 10):
5            while temp % i == 0:
6                temp //= i
7
8        if temp > 1:
9            return "-1"
10
11        n = len(num)
12        rem = [0] * (n + 1)
13        rem[0] = t
14        pos = n - 1
15
16        num_list = list(num)
17        for i in range(n):
18            if num_list[i] == "0":
19                pos = i
20                break
21            rem[i + 1] = rem[i] // math.gcd(rem[i], int(num_list[i]))
22
23        if rem[n] == 1:
24            return num
25
26        for i in range(pos, -1, -1):
27            while True:
28                num_list[i] = chr(ord(num_list[i]) + 1)
29                if num_list[i] > "9":
30                    break
31
32                t_now = rem[i] // math.gcd(rem[i], int(num_list[i]))
33                k = 9
34
35                for j in range(n - 1, i, -1):
36                    while t_now % k != 0:
37                        k -= 1
38                    t_now //= k
39                    num_list[j] = str(k)
40
41                if t_now == 1:
42                    return "".join(num_list)
43
44        ans = []
45        original_t = t
46        for i in range(9, 1, -1):
47            while original_t % i == 0:
48                ans.append(str(i))
49                original_t //= i
50
51        ans_str = "".join(ans)
52        padding = max(n + 1 - len(ans_str), 0)
53        ans_str += "1" * padding
54
55        return ans_str[::-1]