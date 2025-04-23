class Solution:
    def countLargestGroup(self, n: int) -> int:
        hashed={} # key (num) : value(sum)
        for num in range(1,n+1):
            xsum = sum([int(x) for x in list(str(num))])
            hashed[num] = xsum
        
        grouped = defaultdict(list)
        for key , val in hashed.items():
            grouped[val].append(key)
            
        lengths = [len(x) for x in list(grouped.values())]

        maximum = max(lengths)
        count = Counter(lengths)
        return count[maximum]

        

        
        