class Solution:
    def numTrees(self, n: int) -> int:
        # numtree of 4 nodes = left subtree 0 nodes * right subtree with 3 nodes 
        #                   + left subtree of 1 nodes * right subtree with 2 nodes
 # numtree[4] = numtree[0] * numtree[3]  #first value is root
 #              + numtree[1]* numtree[2] + # second value is  root  
 #               +numtree[2] * numtree[1 ]  # third value is root 
 #                +numtree[3] * numtree[1 ]  # forth value is root 

 # dynamic programming
        numTree = [1] *(n+1)
        #0 nodes = 1 tree , 1 nodes = 1 tree
        for nodes in range(2,n+1):
            total = 0
            for root in range(1,nodes+1):
                left = root-1
                right = nodes - root
                total += numTree[left] * numTree[right]
            numTree[nodes] = total

        return numTree[n]




