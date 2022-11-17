class DisJointSets():
    def __init__(self,N):
        # Initially, all elements are single element subsets
        self._parents = [node for node in range(N)]
        self._ranks = [1 for _ in range(N)]
    
    def find(self, u):
        while u != self._parents[u]: 
            # path compression technique
            self._parents[u] = self._parents[self._parents[u]]
            u = self._parents[u]
        return u
    
    def connected(self, u, v):
        return self.find(u) == self.find(v)
    
    def union(self, u, v):
        # Union by rank optimization
        root_u, root_v = self.find(u), self.find(v)
        if root_u == root_v:
            return 0
        if self._ranks[root_u] > self._ranks[root_v]:
            self._parents[root_v] = root_u
        elif self._ranks[root_v] > self._ranks[root_u]:
            self._parents[root_u] = root_v
        else:
            self._parents[root_u] = root_v
            self._ranks[root_v] += 1
        return 1

