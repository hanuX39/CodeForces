https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/

class Graph:
    def __init__(self,num_vertices):
        self.vertices = num_vertices
        self.graph = []
    
    def addedge(self, src, dest, wght):
        return self.graph.append([src, dest, wght])
    
    def find(self,parent,i):
        if parent[i] == i:
            return i
        return self.find(parent,parent[i])
    
    def union(self, parent, rank, x, y):
        xroot = self.find(parent,x)
        yroot = self.find(parent,y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal(self):
        i,e = 0,0
        result = []
        parent, rank = [], []

        self.graph = sorted(self.graph, key = lambda x: x[2])
        print(self.graph)

        for node in range(self.vertices):
            parent.append(node)
            rank.append(0)

        while(e < self.vertices - 1):
            src, dest, wght = self.graph[i]
            i += 1

            x = self.find(parent, src)
            y = self.find(parent, dest)

            if x != y:
                e += 1
                result.append([src, dest, wght])
                self.union(parent, rank, x, y)
        print('Following is the MST of graph')
        for node in result:
            print('{} <---> {} ==== weight {}'.format(node[0],node[1],node[2]))


g = Graph(6)
g.addedge(0,1,15)
g.addedge(0,2,10)
g.addedge(0,5,3)
g.addedge(1,4,13)
g.addedge(1,2,9)
g.addedge(2,3,20)
g.addedge(3,5,10)
g.addedge(4,5,5)
g.addedge(1,5,7)


g.kruskal()

            
