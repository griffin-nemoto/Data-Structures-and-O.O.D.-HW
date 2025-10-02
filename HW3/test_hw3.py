import unittest
import hw3
class Testhw3(unittest.TestCase):
    def test_generate_list(self):
        size = 10
        list1, list2 = hw3.generate_lists(size)
        self.assertEqual(len(list1),size)
    def test_find_common(self):
        list1 = [1,2,3,4,5]
        list2 = [5,6,7,8,9]
        self.assertEqual(hw3.find_common(list1,list2),1)
    def test_find_common_efficient(self):
        list1 = [1,2,3,4,5]
        list2 = [5,6,7,8,9]
        self.assertEqual(hw3.find_common_efficient(list1,list2),1)
