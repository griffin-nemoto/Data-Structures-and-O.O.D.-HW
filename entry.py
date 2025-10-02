class Entry:
    def __init__(self, item, priority):
        """Creates Entry object"""

        self.item = item
        self.priority = priority

    def __eq__(self, other):
        """Returns True if self and other have same priority"""
        
        if isinstance(other, Entry):
            return self.priority == other.priority

    def __lt__(self, other):
        """Returns True if self has a lower priority than other"""

        if isinstance(other, Entry):
            return self.priority < other.priority
        
    def __le__(self, other):
        """Returns True if self has a priority less than or equal to other"""

        if isinstance(other, Entry):
            return self.priority <= other.priority
        
    def __repr__(self):
        """Returns string representation of Entry object"""

        return f'Entry(item={self.item}, priority={self.priority})'
