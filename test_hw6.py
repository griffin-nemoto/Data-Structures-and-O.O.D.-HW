import unittest
from hw6 import bubble_sort, selection_sort, insertion_sort, merge

class SortingTestFactory:
    """This class provides methods to generate test cases for sorting algorithms."""
    def setUp(self, sorting_alg):
        """
        Set up the sorting algorithm for testing.
        Args:
            sorting_alg (function): The sorting algorithm to be tested.
        """
        self.sorting_alg = sorting_alg

    def test_merge(self):
        """ Test case for the merge function to verify that it correctly merges three sorted rows."""
        # Define the sorted rows to test
        matrix = [[1, 4, 7, 10], [2, 5, 8, 11],[3, 6, 9, 12]] 
        # Expected merged result
        expected_merged = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

        # Call the merge function
        self.assertEqual(expected_merged, merge(matrix[0],matrix[1],matrix[2]))

    def is_sorted(self, L):
        """ Check if a list is sorted. """
        return all(L[i] <= L[i + 1] for i in range(len(L) - 1))

    def test_empty(self):
        """Tests algorithm with empty lists"""

        matrix = [[], [],[]] 
        self.assertEqual(self.sorting_alg(matrix), ([],0))
    
    def test_sorted(self):
        """Tests algorithm with sorted list"""

        matrix = [[1, 4, 7, 10], [1, 4, 7, 10],[1, 4, 7, 10]] 
        self.assertEqual(self.sorting_alg(matrix), ([1, 4, 7, 10],0))
    
    def test_reverse_sorted(self):
        """Tests algorithm with reverse sorted list"""

        matrix = [[10,7,4,1], [10,7,4,1],[10,7,4,1]] 
        self.assertEqual(self.sorting_alg(matrix),([1,4,7,10],6))
    
    def test_random(self):
        """Tests algorithm with randomly sorted list"""

        matrix = [[7,1,10,4], [7,1,10,4],[7,1,10,4]] 
        self.assertEqual(self.sorting_alg(matrix), ([1,4,7,10],3))
    

class TestBubble(SortingTestFactory, unittest.TestCase):
    """Test class for the bubble sort algorithm."""

    def setUp(self):
        """Set up the bubble sort algorithm for testing."""
        super().setUp(bubble_sort)


class TestInsertion(SortingTestFactory, unittest.TestCase):
    """Test class for the insertion sort algorithm"""

    def setUp(self):
        '''Set up the insertion sort algorithm for testing'''
        super().setUp(insertion_sort)

class TestSelection(SortingTestFactory, unittest.TestCase):
    """Test class for the selection sort algorithm"""

    def setUp(self):
        '''Set up the selection sort algorithm for testing'''
        super().setUp(selection_sort)

    def test_random(self):
        '''Tests selection sort algorithm with randomly sorted list'''

        matrix = [[7,1,10,4], [7,1,10,4],[7,1,10,4]] 
        self.assertEqual(self.sorting_alg(matrix), ([1,4,7,10], 3))

    def test_reverse_sorted(self):
        '''Tests selection sort algorithm with reverse sorted list'''
        
        matrix = [[10,7,4,1], [10,7,4,1],[10,7,4,1]] 
        self.assertEqual(self.sorting_alg(matrix),([1,4,7,10],2))
        

if __name__ == "__main__":
    unittest.main()
