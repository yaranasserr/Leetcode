# Last updated: 7/9/2025, 2:56:21 PM
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {} # sortedword : list of words 

        for s in strs :
            key="".join(sorted(s))
            if key not in anagrams :
                anagrams[key]=[]

            anagrams[key].append(s)

        return list(anagrams.values())

            
        