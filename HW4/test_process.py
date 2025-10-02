import unittest
import process

class TestProcess(unittest.TestCase):

    def test_init_name(self):
        p = process.Process('hi')
        
        self.assertEqual(p.pid,'hi')
        self.assertEqual(p.cycles,100)
        self.assertEqual(p.link,None)
        self.assertEqual(p.prev,None)


    def test_init_name_and_cycles(self):
        p = process.Process('hi', 300)
        
        self.assertEqual(p.pid,'hi')
        self.assertEqual(p.cycles,300)
        self.assertEqual(p.link,None)
        self.assertEqual(p.prev,None)

        
    def test_eq(self):

        p1 = process.Process('Same')
        p2 = process.Process('Same')
        p3 = process.Process('Not Same')
        p4 = process.Process('Different')
        
        self.assertEqual(p1,p2)
        self.assertNotEqual(p3,p4)

    def test_repr(self):
        p = process.Process('A', 200)

        self.assertEqual(p.__repr__(),'Process(A, 200)')
