from collections import defaultdict
 
class Graph():
 
    def __init__(self, V, edges=[]):
        self.V = V
        self.graph = defaultdict(list)
        for edge in edges:
            self.addEdge(*edge)
 
    def addEdge(self, v, w):
        # Add w to v list.
        self.graph[v].append(w) 
        # Add v to w list.
        self.graph[w].append(v) 
 
    # A recursive function that uses visited[] 
    # and parent to detect cycle in subgraph 
    # reachable from vertex v.
    def isCyclicUtil(self, v, visited, parent):
 
        # Mark current node as visited
        visited[v] = True
 
        # Recur for all the vertices adjacent 
        # for this vertex
        for i in self.graph[v]:
            # If an adjacent is not visited, 
            # then recur for that adjacent
            if visited[i] == False:
                if self.isCyclicUtil(i, visited, v) == True:
                    return True
 
            # If an adjacent is visited and not 
            # parent of current vertex, then there 
            # is a cycle.
            elif i != parent:
                return True
 
        return False
 
    # Returns true if the graph is a tree, 
    # else false.
    def isTree(self):
        # Mark all the vertices as not visited 
        # and not part of recursion stack
        visited = [False] * self.V
 
        # The call to isCyclicUtil serves multiple 
        # purposes. It returns true if graph reachable 
        # from vertex 0 is cyclic. It also marks 
        # all vertices reachable from 0.
        if self.isCyclicUtil(0, visited, -1) == True:
            return False
 
        # If we find a vertex which is not reachable
        # from 0 (not marked by isCyclicUtil(), 
        # then we return false
        for i in range(self.V):
            if visited[i] == False:
                return False
 
        return True
n, m = 7, 8
edges = [(0, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (0, 5), (0, 3)]

# Now we can create a Graph object with our list of edges
original_graph = Graph(7, edges)
sample_output_edges = [
    (1, 2), 
    (5, 6),
    (0, 1),
    (0, 3),
    (0, 5)
]
original_graph.isTree()
new_graph = Graph(7, sample_output_edges)
print(new_graph.isTree())
