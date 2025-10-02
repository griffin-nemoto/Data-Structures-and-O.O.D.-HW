import unittest
from dictionary_bst import Node
from dictionary_bst import DictionaryBST

class test_node(unittest.TestCase):

    def test_init(self):
        '''Tests assignment for initializing a node instance'''

        n1 = Node('apple', 'red fruit')

        self.assertEqual(n1.height,0)
        self.assertEqual(n1.length, 1)

        self.assertEqual(n1.left, None)
        self.assertEqual(n1.right, None)

        self.assertEqual(n1.word,'apple')
        self.assertEqual(n1.meaning,'red fruit')


class test_dictionary_bst(unittest.TestCase):
    
    def test_init_empty(self):
        '''Tests intializing when entries is empty'''

        entries = dict()
        d1 = DictionaryBST(entries)
        
        self.assertEqual(d1.root, None)

    def test_init_one(self):
        '''Tests initializing when entries is not empty'''

        entries = dict()
        entries['apple'] = 'red fruit'

        d1 = DictionaryBST(entries)

        self.assertEqual(d1.root, Node('apple', 'red fruit'))
        

    def test_insert_new(self):
        '''Tests that unique nodes are inserted properly'''

        entries = dict()
        entries['apple'] = 'red fruit'

        d1 = DictionaryBST(entries)

        n1 = Node('banana', 'yellow fruit')
        d1.insert('banana', 'yellow fruit')

        self.assertEqual(d1.root.right, n1)

        
    def test_insert_duplicate(self):
        '''Tests that duplicated nodes inserted aren't added to the BST'''

        entries = dict()
        entries['apple'] = 'red fruit'

        d1 = DictionaryBST(entries)

        n1 = Node('apple', 'red fruit')
        d1.insert('apple', 'red fruit')

        self.assertEqual(d1.root, n1)
        self.assertEqual(d1.root.left, None)
        self.assertEqual(d1.root.right, None)

    def test_search(self):
        '''Tests searching for root node, and nodes on left and right of root node'''

        entries = dict()

        entries['banana'] = 'yellow fruit'
        entries['apple'] = 'red fruit'
        entries['orange'] = 'orange fruit'
        
        d1 = DictionaryBST(entries)

        self.assertEqual(d1.search('apple'), 'red fruit')
        self.assertEqual(d1.search('banana'), 'yellow fruit')
        self.assertEqual(d1.search('orange'), 'orange fruit')

    def test_rebalance(self):
        '''Tests auto-balancing of BST'''

        entries = dict()
        d1 = DictionaryBST(entries)

        d1.insert('apple', 'red')
        d1.insert('banana', 'yellow')
        d1.insert('cranberry', 'red also')
        d1.insert('dairy', 'milky')
        d1.insert('elephant', 'big')

        self.assertEqual(d1.root, Node('cranberry', 'red also'))
        self.assertEqual(d1.root.left.left, Node('apple', 'red'))
        self.assertEqual(d1.root.left, Node('banana', 'yellow'))
        self.assertEqual(d1.root.right, Node('dairy', 'milky'))
        self.assertEqual(d1.root.right.right, Node('elephant', 'big'))
        self.assertEqual(d1.root.height, 2)

    def test_print_alphabetical(self):
        '''Tests that print_alphabetical works as intended'''

        entries = dict()
        d1 = DictionaryBST(entries)

        d1.insert('apple', 'red')
        d1.insert('banana', 'yellow')
        d1.insert('cranberry', 'red also')

        self.assertEqual(d1.print_alphabetical(), [("apple", "red"),    ("banana", "yellow"),
    ("cranberry", "red also")])

if __name__ == '__main__':
    unittest.main()
