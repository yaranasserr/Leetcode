from collections import defaultdict, deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        # Create adjacency list for patterns
        nei = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                nei[pattern].append(word)

        # BFS setup
        visit = set([beginWord])
        q = deque([beginWord])
        res = 1

        # Perform BFS
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res

                # Check neighbors via patterns
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            
            res += 1

        return 0
