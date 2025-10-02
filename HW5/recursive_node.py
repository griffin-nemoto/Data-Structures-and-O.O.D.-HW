###############################################################################
# init, and repr  are implemented for you. You should implement the other     #
# methods recursively.                                                        #
###############################################################################
class Node:
    """Reucrsively implementes Linked List functionality"""
    def __init__(self, data, link=None):
        """Instantiates a new Node with given data"""
        self.data = data
        self.link = link

    def __repr__(self):
        """Returns string representation of node"""
        return f"Node({self.data})"
    
    def __len__(self):
        '''Recursively finds length of the linked list'''

        if self.link is None:
            return 1 
        
        return 1 + len(self.link)

    def get_tail(self):
        """Recursively finds the data stored in the tail of this sublist"""

        if self.link is None:
            return self.data

        return self.link.get_tail()

    
    def add_last(self, data):
        """Recursively adds to end of this sublist"""

        if self.link is None:
            self.link = Node(data)
        else:
            self.link.add_last(data)

    def total(self):
        """Recursively adds all items"""

        if self.link is None:
            return self.data
    
        return self.data + self.link.total()
    
    def remove_last(self):
        """Recursively removes last item in sublist
            Returns a tuple of (new_head, data). The new_head is the
            new head of this sublist after removing the tail.

            OUTPUT
            ------
            new_head, tail_data
                * new_head: Node or None
                    The new link for whatever node called this function
                
                * tail_data: Any
                    The data that was found in the tail node
        """
        if self.link is None:
            return None, self.data

        if self.link.link is None:

            data = self.link.data
            self.link = None

            return self, data
        
        head,tail_data = self.link.remove_last()
        
        return self, tail_data

    def reverse(self, prev):
        """Recursively reverse list"""

        if self.link is None:
            
            self.link = prev
            return self
        hold = self.link
        self.link = prev
        return hold.reverse(self)
        


