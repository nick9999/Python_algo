class Graph():

    def __init__(self,v):
        self.v = v
        self.graph = []

    def add_edge(self,u,v,w):
        self.graph.append([u,v,w])

    def _find(self,parent,i):
        if(parent[i]==i):
            return i
        return self._find(parent, parent[i])

    def _union(self,x,y, parent, rank):
        root_x = self._find(parent, x)
        root_y = self._find(parent, y)
        if rank[root_x] < rank[root_y]:
            parent[root_x] =root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    def kruskal_mst(self):
        parent , rank = [], []
        for v in range(self.v):
            parent.append(v)
            rank.append(v)
        i,e=0,0
        mst = []
        self.graph = sorted(self.graph, key=lambda x: x[2])
        while e < self.v-1:
            u,v,w=self.graph[i]
            parent_u = self._find(parent,u)
            parent_v = self._find(parent,v)
            if parent_u != parent_v:
                e += 1
                mst.append([u,v,w])
                self._union(u,v,parent,rank)
            i += 1
        return mst

    def prims_mst(self):
        pass

if __name__ == '__main__':
    g = Graph(4)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 4)
    mst = g.kruskal_mst()
    print mst