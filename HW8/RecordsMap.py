# See assignment for class attributes.
# Remember to include docstrings.
# Start with unittests

class LocalRecord:
    def __init__(self, pos, min=None, max=None, precision = 0): 
        '''Creates LocalRecord object'''
        lat, long = pos
        self.pos = round(lat,precision), round(long, precision)

        self.max = max
        self.min = min

    def add_report(self, temp): 
        '''Updates max/min temp if given temp is greater/less '''

        if temp > self.max:
            self.max = temp

        if temp < self.min:
            self.min = temp

    def __eq__(self, other): 
        return hash(self.pos) == hash(other.pos)

    def __hash__(self): 
        return hash(self.pos)

    def __repr__(self):
        return f"Record(pos={self.pos}, max={self.max}, min={self.min}"

class RecordsMap:
    def __init__(self): 
        '''Initializes RecordsMap object'''
        self.n_buckets = 8
        self._buckets = [[] for i in range(self.n_buckets)]
        self._len = 0


    def __len__(self): 
        '''Returns number of key,value pairs in RecordsMap'''
        return self._len

    def add_report(self, pos, temp):
        '''Updates min/max of pos if necessary, if pos doesn't exist in RecordsMap, a new record is added with given temp'''
        record = LocalRecord(pos,temp,temp)
        bucket = self._buckets[hash(record) % self.n_buckets]

        for key in bucket:

            if key == record:
                key.add_report(temp)
                return
            
        bucket.append(record)
        self._len += 1

        if self._len >= 2*self.n_buckets:
            self._rehash(self.n_buckets * 2)


    def __getitem__(self, pos): 
        '''Returns tuple of min,max for given position, raises KeyError if position is not in RecordsMap'''
        record = LocalRecord(pos)
        bucket =  self._buckets[hash(record) % self.n_buckets]

        for key in bucket:

            if key == record:
                return (key.min,key.max)
        
        raise KeyError 
  
    def __contains__(self, pos):
        '''Checks membership for given position in RecordsMap'''
        record = LocalRecord(pos)
        bucket = self._buckets[hash(record) % self.n_buckets]

        return record in bucket

    def _rehash(self, m_new): 
        '''Rehashes self._buckets to length m_new'''

        new_buckets = [[] for i in range(m_new)]

        for bucket in self._buckets:
            for record in bucket:

                new_index = hash(record) % m_new
                new_buckets[new_index].append(record)

        self.n_buckets = m_new
        self._buckets = new_buckets
