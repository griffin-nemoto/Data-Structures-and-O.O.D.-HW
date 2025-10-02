from entry import Entry

class Heap:
    def __init__(self):
        """Creates Heap object"""

        self._L = []
        self._idx = dict()

    def __len__(self):
        """Returns number of items in heap"""

        return len(self._L)

    def __iter__(self):
        """Yields and removes each entry in the PQ in increasing order """

        copy = Heap()

        for entry in self._L:

            copy.insert(entry.item, entry.priority)

        while copy._L:

            yield copy.remove_min()
        

    def idx_parent(self, idx):
        """Returns index of the parent for the entry at given index"""

        p_idx = (idx - 1) // 2

        return p_idx if idx > 0 else None

    def idx_left(self, idx):
        """Returns index of left child for entry at given index"""
        
        left_idx = idx*2 + 1

        return left_idx if left_idx < len(self) else None  # Returns index if the index exists in the PQ
    
    def idx_right(self, idx):
        """Returns index of right child for entry at given index"""

        right_idx = idx*2 + 2

        return right_idx if right_idx < len(self) else None

    def idx_min_child(self, idx):
        """Returns the index of the child of the entry at the given index with the lower priority"""

        right_idx = self.idx_right(idx)
        left_idx = self.idx_left(idx)
        if left_idx is None and right_idx is None:
            return None

        elif left_idx is None:
            return right_idx

        elif right_idx is None:
            return left_idx
        
        elif self._L[right_idx] <= self._L[left_idx]:
            return right_idx
            
        return left_idx
        
    def insert(self, item, priority):
        """Inserts entry with given data into the heap"""

        self._L.append(Entry(item,priority))
        self._idx[item] = len(self) - 1

        self._upheap(len(self) - 1)
        

    def remove_min(self):
        """Removes lowest priority entry from the heap""" 

        if len(self) == 0:

            return None
        
        min_entry = self._L[0]
        
        if len(self) == 1:
            
            self._idx.pop(min_entry.item)
            return self._L.pop()
        
       
        last = self._L.pop()

        self._idx.pop(min_entry.item)
        
        self._L[0] = last
        self._idx[last.item] = 0

        self._downheap(0)

        return min_entry


    def change_priority(self, item, priority):
        """Changes the priority of the entry matching 'item' to new value and returns new index in PQ"""
        item_index = self._idx[item]
        old_priority = self._L[item_index].priority
        self._L[item_index].priority = priority

        if priority < old_priority:      

            self._upheap(item_index)

        else:

            self._downheap(item_index)

        new_idx = self._idx[item]   # Index value in dictionary is swapped in _swap function
                                    # so this holds the new value after up/downheap 

        return new_idx
        

    def _swap(self, i, j):
        """Swaps entries at given indices and updates dictionary"""

        entries = self._L

        item1, item2 = entries[i].item, entries[j].item     # Need to find items to use as keys in _idx to swap values

        entries[i], entries[j] = entries[j], entries[i]

        self._idx[item1], self._idx[item2] = self._idx[item2], self._idx[item1]

    def _upheap(self, idx):
        """Checks entry against parent and swaps out of order entries"""

        p_idx = self.idx_parent(idx)
        
        if p_idx is not None and self._L[idx] < self._L[p_idx]:

            self._swap(idx, p_idx)  
            self._upheap(p_idx)

    def _downheap(self, idx):
        """Checks entry against smaller of its children and swaps out of order entries"""

        min_child_idx = self.idx_min_child(idx)

        if min_child_idx and self._L[idx] > self._L[min_child_idx]:

            self._swap(idx, min_child_idx)
            self._downheap(min_child_idx)


    @staticmethod
    def heapify(entries):
        """Transforms given list of entries into a heap and returns new heap"""

        new_heap = Heap()

        new_heap._L = entries[:]
        new_heap._idx = {entry.item : idx for idx, entry in enumerate(entries)}

        for i in reversed(range(len(entries) // 2)):

            new_heap._downheap(i)

        return new_heap