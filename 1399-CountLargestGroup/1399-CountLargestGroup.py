# Last updated: 4/23/2025, 2:08:51 PM
class Solution:
    def countLargestGroup(self, n: int) -> int:
        hashed={} # key (num) : value(sum)
        for num in range(1,n+1):
            xsum = sum([int(x) for x in list(str(num))])
            hashed[num] = xsum

        print(hashed.items())

        
        grouped = defaultdict(list)
        for key , val in hashed.items():
            grouped[val].append(key)
            
        res = list(grouped.values())
        print(res)
        lengths = [len(x) for x in res]
        print(lengths)
        maximum = max(lengths)
        count = Counter(lengths)
        return count[maximum]

        

        
        