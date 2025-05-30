class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrences = {}
        for n in arr :
            occurrences[n] = 1+occurrences.get(n,0)



        # occurrences = {item: arr.count(item) for item in set(arr)} # frequency
        print(set(occurrences.values()))
      
        return len(occurrences.values()) == len(set(occurrences.values()))
            
        