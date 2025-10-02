from queue import Queue

class Graph():


    def __init__(self, V=None, E=None):
        '''Creates Graph object'''

        raise NotImplementedError
    
    def is_connected(self, v1, v2):
        '''Returns True if v1 and v2 are connected by a path, otherwise returns False'''

        tree = self.bfs(v1)

        return v2 in tree

        

    def bfs(self, v):
        '''Returns dictionary of breadth-first search tree'''

        tree = {}
        visit = Queue()

        visited = set()

        visit.put((None, v))

        while not visit.empty():

            prev, curr = visit.get()
            if curr not in visited:

                visited.add(curr)
                tree[curr] = prev

            for vertex in self.nbrs(curr):

                if vertex not in visited:

                    visit.put((curr, vertex))
        
        return tree



    def shortest_path(self, v1, v2):
        '''Returns shortest path between v1 and v2'''

        tree = self.bfs(v1)

        if v2 not in tree:
            return None     # This means that the two vertices are not connected, and thus there is no path between them
        
        path = []
        curr = v2 

        while curr is not None: # The previous node from v1 is None, so this works to allow v1 to be added to the path

            path.append(curr)
            curr = tree[curr]
        
        return path

    def count_trees(self):
        '''Returns a list of each unique tree in the graph'''

        trees = []
        visited = set()


        for vertex in self:

            if vertex not in visited:

                curr_tree = self.bfs(vertex)
                trees.append(curr_tree)

                visited.update(curr_tree.keys())

        return trees, len(trees) 



class AdjacencySetGraph(Graph):

    def __init__(self, V, E):
        '''Creates AdjacencySet graph'''

        if V is None and E is None:

            V = set()
            E = set()

        self._n = dict()

        for v in V:
            self.add_vertex(v)

        for e in E:
            self.add_edge(e)


    def __iter__(self):
        '''Returns each vertex in the graph'''

        for v in self._n:
            yield v

    def add_vertex(self, v):
        '''Adds vertex to graph'''

        self._n[v] = set()

    def add_edge(self, e):
        '''Adds edge to graph'''

        v1, v2 = e

        self._n[v1].add(v2)
        self._n[v2].add(v1)

    def nbrs(self, v):
        '''Returns neighbors of v'''

        return self._n[v]
    
class EdgeSetGraph(Graph):

    def __init__(self, V=None, E=None):
        '''Creates EdgeSet object'''

        if V is None and E is None:
            V = set()
            E = set()
            
        self.vertices = set()
        self.edges = set()

        for v in V:
            self.add_vertex(v)

        for e in E:
            self.add_edge(e)


    def __iter__(self):
        '''Iterates through each vertex in the graph'''

        for v in self.vertices:
            yield v 

    def add_vertex(self, v):
        '''Adds vertex to graph'''

        self.vertices.add(v)

    def add_edge(self, e):
        '''Adds edge to graph'''

        v1,v2 = e
        
        self.edges.add((v1,v2))
        self.edges.add((v2,v1))

    def nbrs(self, v):
        '''Returns neighbors of given vertex'''

        return (v2 for v1,v2 in self.edges if v1 == v)

    

    



        
