# Last updated: 12/12/2025, 8:51:57 PM
1class Solution:
2    def countMentions(
3        self, numberOfUsers: int, events: List[List[str]]
4    ) -> List[int]:
5        events.sort(key=lambda e: (int(e[1]), e[0] == "MESSAGE"))
6        count = [0] * numberOfUsers
7        next_online_time = [0] * numberOfUsers
8        for event in events:
9            cur_time = int(event[1])
10            if event[0] == "MESSAGE":
11                if event[2] == "ALL":
12                    for i in range(numberOfUsers):
13                        count[i] += 1
14                elif event[2] == "HERE":
15                    for i, t in enumerate(next_online_time):
16                        if t <= cur_time:
17                            count[i] += 1
18                else:
19                    for idx in event[2].split():
20                        count[int(idx[2:])] += 1
21            else:
22                next_online_time[int(event[2])] = cur_time + 60
23        return count