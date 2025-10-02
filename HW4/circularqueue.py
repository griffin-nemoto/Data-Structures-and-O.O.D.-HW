from process import Process

class CircularQueue:
    """A circular queue to allow us to run processes turn-by-turn"""
    def __init__(self, processes = None):
        '''Initializes CircularQueue object with no head, empty dictionary, and length of 0
        If user passses list of Process objects, they will be added to the CircularQueue'''

        self._head = None
        self._len  = 0
        self._d_processes = dict()

        if processes is not None: 
            for process in processes: # Adds each Process in processes to the CQ given there was an argument passed
                self.add_process(process)
    
    def __len__(self):
        '''Returns current length of CircularQueue'''

        return self._len
    
    def __repr__(self):
        '''Returns string representation of current CQ with each process's pid and cycles'''

        node = self._head
        cq_str = repr(node) + ', '

        while node.link is not self._head:

            node = node.link
            cq_str += repr(node) + ', '

        cq_str = cq_str[0:-2]

        return f'CircularQueue({cq_str})'

    def add_process(self, process: Process):
        '''Adds a Process to CQ, and increments length, and updates dictionary
        If CQ was previously empty, assigns given process to CQ._head'''

        self._len += 1
        self._d_processes[process.pid] = process

        if self._len == 1:

            self._head = process
            process.link = process
            process.prev = process
        else:

            process.prev = self._head.prev
            self._head.prev.link = process
            self._head.prev = process
            process.link = self._head
    
    def remove_process(self, process):
        '''Removes and returns a given process from CQ, decrementing length and removing from dictionary
        Raises error if CQ is empty
        If removing the last process in CQ, assigns head to None'''

        if self._len == 0:
            raise RuntimeError('Removing From Empty CircularQueue')
        
        self._d_processes.pop(process.pid)

        if self._len == 1:

            self._head = None
        else:

            if self._head == process:
                self._head = process.link

            process.prev.link = process.link
            process.link.prev = process.prev

        self._len -= 1

        return process

    

    def kill(self, pid):
        '''Removes and returns process from CQ using _d_processes dictionary and a given pid
        Fails if CQ is empty
        Assigns head to None if last process is being removed
        Updates length and dictionary'''

        if self._len == 0: 
            raise RuntimeError('Removing From Empty CircularQueue')
        
        process = self._d_processes[pid]

        self._d_processes.pop(pid)

        if self._len == 1:

            self._head = None
        else:
            
            if self._head == process:
                self._head = process.link

            process.prev.link = process.link
            process.link.prev = process.prev

        self._len -= 1

        return process

    
 



    def run(self, n_cycles):
        """Runs circular queue for n_cycles, giving each process 1 cycle at a time"""
        n_remaining = n_cycles
        return_strings = []   # Using an intermediate list since appending to a string is O(n)

        while n_remaining:
            self._head.cycles -= 1

            if self._head.cycles == 0:
                return_strings.append(f"{self._head.pid} finished after {n_cycles-n_remaining+1} computational cycles.")
                self.remove_process(self._head)

            else:
                self._head = self._head.link
            
            n_remaining -= 1

        return '\n'.join(return_strings)
