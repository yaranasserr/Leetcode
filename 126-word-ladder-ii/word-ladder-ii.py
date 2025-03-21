from collections import defaultdict, deque
from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        depthmap={}
        ans = []
        # dfs for backtracking
        def dfs(word,seq):
            if word == beginWord :
                ans.append(seq[::-1])
                return 

            steps = depthmap[word]
            for i in range(len(word)):
                original = word[i]
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    word = word[:i] + ch + word[i+1:]
                    if word in depthmap and depthmap[word] +1 == steps :
                        seq.append(word)
                        dfs(word,seq)
                        seq.pop()
                word = word[:i] +original +word[i+1:]

         #bfs 

        wordset = set(wordList)
        q= deque([beginWord])
        depthmap[beginWord] = 1

        wordset.discard(beginWord)

        while q :
            word = q.popleft()
            steps = depthmap[word]
            if word == endWord:
                break

            for i in range(len(word)):
                original = word[i]
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    
                    word = word[:i] + ch + word[i+1:]
                    if word in wordset:
                        q.append(word)
                        wordset.discard(word)
                        depthmap[word] = steps+1

                word = word[:i] + original + word[i+1:]
        if endWord in depthmap :
            seq = [endWord]
            dfs(endWord,seq)

        return ans 


            

                    





                


        return ans 

        
        # if endWord not in wordList:
        #     return []
        
        # wordList = set(wordList)  # Use a set for O(1) lookups
        # wordList.add(beginWord)  # Ensure `beginWord` is in the list
        
        # # Step 1: Build adjacency list for pattern-based transformations
        # nei = defaultdict(list)
        # for word in wordList:
        #     for j in range(len(word)):
        #         pattern = word[:j] + "*" + word[j+1:]
        #         nei[pattern].append(word)
        
        # # Step 2: BFS to find the shortest path graph
        # q = deque([[beginWord]])  # Queue stores paths, not just words
        # visited = set()  # Track visited words
        # parents = defaultdict(set)  # Store predecessors for backtracking
        # found = False  # Flag to stop BFS when endWord is reached
        
        # while q and not found:
        #     next_level = set()
        #     for _ in range(len(q)):
        #         path = q.popleft()
        #         word = path[-1]  # Get the last word in the current path
                
        #         for j in range(len(word)):
        #             pattern = word[:j] + "*" + word[j+1:]
        #             for nei_word in nei[pattern]:
        #                 if nei_word not in visited:
        #                     next_level.add(nei_word)
        #                     parents[nei_word].add(word)
        #                     q.append(path + [nei_word])
        #                 if nei_word == endWord:
        #                     found = True  # Stop BFS when we reach `endWord`
            
        #     visited.update(next_level)  # Mark words visited after this level
        
        # # Step 3: Backtracking DFS to reconstruct all shortest paths
        # res = []
        
        # def backtrack(word, path):
        #     if word == beginWord:
        #         res.append(path[::-1])  # Reverse the path to start from beginWord
        #         return
        #     for parent in parents[word]:
        #         backtrack(parent, path + [parent])
        
        # if found:
        #     backtrack(endWord, [endWord])
        
        # return res
