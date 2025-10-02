import trib
import unittest

class TestTrib(unittest.TestCase):

    def test_first_ten(self):
        '''First ten values in tribonacci sequence are correct'''
        solution = {1:0, 2:0, 3:1, 4:1, 5:2, 6:4, 7:7, 8:13, 9:24, 10:44}

        for val in solution:
            self.assertEqual(trib.trib(val),solution[val])
    

    def test_hundred(self):
        '''Tests 100th value in tribonacci sequence'''
        self.assertEqual(trib.trib(100), 28992087708416717612934417)

    

if __name__ == '__main__':
    unittest.main()
