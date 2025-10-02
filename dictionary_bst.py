class Node:
    """
    A class to represent a node in the tree.
    """
    def __init__(self, word, meaning):
        '''Creates node object'''
        self.word = word
        self.meaning = meaning
        self.left = None
        self.right = None
        self.height = 0
        self.length = 1

    def __eq__(self, other):
        '''Overwrites __eq__ function for test class so if word and meaning match, nodes are equal'''
        if isinstance(other, Node):
    
            return self.word == other.word and self.meaning == other.meaning
        return False


    
    
                


class DictionaryBST:
    """
    A class to represent a dictionary using self-balancing trees.
    
    Methods:
        insert(word, meaning): Insert a word and its meaning into the dictionary.
        search(word): Search for a word in the dictionary and return its meaning.
        print_alphabetical(): Return all dictionary entries in alphabetical order.
    """
    def __init__(self, entries: dict[str, str] | None = None):
        """
        Parameters:
        entries (dict[str, str] | None, optional): A dictionary with string words and meanings.
                                                  Defaults to None if not provided.
        """
        self.root = None
        if entries is not None:

            for word, meaning in entries.items():

                self.insert(word,meaning)


    def insert(self, word, meaning):
        """
        Insert a word and its meaning into the tree. If inserting a duplicate word updates the meaning.
        
        Args:
            word (str): The word to insert.
            meaning (str): The meaning of the word.
        """


        if self.root is None:

            self.root = Node(word, meaning)
        else:
            self.root = self._insert(word,meaning, self.root)

    def _insert(self, key, value, node):
        '''Inserts a new node into the tree or replaces meaning if already present in tree'''
        

        if node.word == key:
            node.meaning = value

        elif key < node.word:
            if node.left is None:
                node.left = Node(key,value)

            else: 
                node.left = self._insert(key,value,node.left)

        else:
            if node.right is None:
                node.right = Node(key, value)
            
            else:
                node.right = self._insert(key,value,node.right)

        self.update(node)
        return self.rebalance(node)
        

    def search(self, word):
        """
        Search for a word in the tree and return its meaning.
        
        Args:
            word (str): The word to search for.
        
        Returns:
            str: The meaning of the word if found, else return None'
        """
        return self._search(word, self.root)
    
    def _search(self, word, node):
        '''Returns given word's meaning'''
        if node is None:
            return None
        
        if node.word == word: 
            return node.meaning
        
        if word < node.word:
            if node.left is not None:
                return self._search(word, node.left)
            
        elif node.right is not None:
            return self._search(word, node.right)
        
        return None
    
    def print_alphabetical(self):
        """
        Retrieve all dictionary entries in alphabetical order.
        
        Returns:
            list of tuple: List of tuples, each containing (word, meaning).
        """

        return list(self.in_order(self.root))    

    def in_order(self, node):
        '''Returns tuples of data from nodes in order'''
        if node.left is not None:
            yield from self.in_order(node.left)

        yield (node.word, node.meaning)

        if node.right is not None:
            yield from self.in_order(node.right)

    # Feel free to implement other helper and private methods

    def rotate_right(self, node):
        '''Rotates tree at 'node' to the right'''

        new_root = node.left
        node.left = new_root.right
        new_root.right = node

        self.update(node)
        self.update(new_root)

        return new_root
    
    def rotate_left(self, node):
        '''Rotates tree at 'node' to the left'''

        new_root = node.right
        node.right = new_root.left
        new_root.left = node

        self.update(node)
        self.update(new_root)

        return new_root
    
    def balance(self, node):
        '''Returns balance factor of node'''
        if node.right is None:
            right = 0
        else:
            right = self._height(node.right)
        if node.left is None:
            left = 0
        else:
            left = self._height(node.left)
        return right - left
    

    def rebalance(self, node):
        '''Balances BST'''

        bal_factor = self.balance(node)

        if bal_factor == 2:
            
            if self.balance(node.right) < 0:
                node.right = self.rotate_right(node.right)
            
            new_root = self.rotate_left(node)
        
        elif bal_factor == -2:

            if self.balance(node.left) > 0:
                node.left = self.rotate_left(node.left)

            new_root = self.rotate_right(node)
        
        else:

            return node
        
        self.update(new_root)
        self.update(new_root.left)
        self.update(new_root.right)

        return new_root
    
    def _update_length(self,node):
        '''Returns length of node'''
        if node is None: 
            return 0
        
        node.length = 1 + (self._update_length(node.left)) + (self._update_length(node.right))
        
        return node.length
    
    def _update_height(self, node):
        '''Updates height of node after a new node is added'''
        node.height =  1 + max(self._height(node.left),self._height(node.right))
    

    def _height(self, node):
        '''Returns height of node'''
        return node.height if node else -1
    
    def update(self, node):
        '''Updates height and length of node'''
        self._update_height(node)
        self._update_length(node)