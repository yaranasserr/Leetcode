class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for w in strs:
            key=''.join(sorted(w))

            if key not in anagrams :
                anagrams[key] = []
            anagrams[key].append(w)

        return list(anagrams.values())
        