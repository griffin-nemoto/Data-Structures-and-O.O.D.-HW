import unittest
import random
from Graph import Graph, EdgeSetGraph, AdjacencySetGraph

class GraphTestFactory():

    def graph(self, V=None, E=None):
        """This should be overridden in subclasses to return a specific graph type"""
        raise NotImplementedError

    def test_graph_construction(self):

        g = self.graph()

        g.add_vertex('A')
        g.add_vertex('B')
        g.add_edge(('A', 'B'))

        self.assertIn('B', g.nbrs('A'))

    def test_is_connected_simple(self):

        V = {'A', 'B', 'C'}
        E = {('A', 'B')}

        g = self.graph(V, E)

        self.assertTrue(g.is_connected('A', 'B'))
        self.assertFalse(g.is_connected('A', 'C'))

    def test_shortest_path(self):

        V = {'A', 'B', 'C', 'D'}
        E = {('A', 'B'), ('B', 'C'), ('C', 'D')}

        g = self.graph(V, E)
        path = g.shortest_path('A', 'D')

        self.assertEqual(len(path) - 1, 3)  # A->B->C->D, length is 3
        self.assertEqual(path[0], 'D')
        self.assertEqual(path[-1], 'A')  # Since path is built backward

    def test_count_trees(self):

        V = {'A', 'B', 'C', 'D', 'E'}
        E = {('A', 'B'), ('B', 'C'), ('D', 'E')}

        g = self.graph(V, E)
        trees, count = g.count_tree()

        self.assertEqual(count, 2)

        all_nodes = set()

        for tree in trees:

            all_nodes.update(tree.keys())

        self.assertEqual(all_nodes, V)


class TestAdjacency(GraphTestFactory,unittest.TestCase):
    
    def graph(self, V = None, E = None):

        if V is None and E is None:

            V = set()
            E = set()

        return AdjacencySetGraph(V,E)

class TestEdge(GraphTestFactory, unittest.TestCase):
    
    def graph(self, V = None, E = None):

        if V is None and E is None:

            V = set()
            E = set()

        return EdgeSetGraph(V,E)

class TestGraphINIT(unittest.TestCase):

    def test_raises_NI(self):
        
        with self.assertRaises(NotImplementedError):
            Graph(set(), set())


if __name__ == '__main__':
    unittest.main()