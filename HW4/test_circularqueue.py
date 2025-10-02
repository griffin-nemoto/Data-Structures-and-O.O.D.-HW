import unittest
from circularqueue import CircularQueue
from process import Process
class TestCircularQueue(unittest.TestCase):
    def assertNodeEqual(self, node, expected, expected_prev, expected_link):

        self.assertEqual(node, expected)
        self.assertEqual(node.prev, expected_prev)
        self.assertEqual(node.link, expected_link)

    def test_init_empty(self):
        cq1 = CircularQueue()
        self.assertEqual(cq1._head,None)
        self.assertEqual(len(cq1),0)

    def test_init_with_processes(self):

        p1 = Process('A')
        p2 = Process('B')
        p3 = Process('C')
        cq2 = CircularQueue([p1,p2,p3])

        self.assertEqual(len(cq2),3)
        node1 = cq2._head
        self.assertNodeEqual(node1, Process('A'), Process('C'), Process('B'))
        
        node2 = cq2._head.link
        self.assertNodeEqual(node2, Process('B'), Process('A'), Process('C'))

        node3 = cq2._head.prev
        self.assertNodeEqual(node3, Process('C'), Process('B'), Process('A'))

    def test_add_process_one(self):
        p1 = Process('A')
        cq3 = CircularQueue()

        cq3.add_process(p1)
        self.assertEqual(len(cq3),1)

        node1 = p1
        self.assertNodeEqual(node1, Process('A'), Process('A'), Process('A'))

    def test_add_process_two(self):
        p1 = Process('A')
        p2 = Process('B')
        cq4 = CircularQueue()

        cq4.add_process(p1)
        cq4.add_process(p2)

        self.assertEqual(len(cq4),2)

        node1 = cq4._head
        self.assertNodeEqual(node1, Process('A'), Process('B'), Process('B'))

        node2 = cq4._head.prev
        self.assertNodeEqual(node2, Process('B'), Process('A'), Process('A'))
        
    def test_add_process_three(self):
        p1 = Process('A')
        p2 = Process('B')
        p3 = Process('C')
        cq5 = CircularQueue()

        cq5.add_process(p1)
        cq5.add_process(p2)
        cq5.add_process(p3)

        self.assertEqual(len(cq5),3)

        node1 = cq5._head
        self.assertNodeEqual(node1, Process('A'), Process('C'), Process('B'))

        node2 = cq5._head.link
        self.assertNodeEqual(node2, Process('B'), Process('A'), Process('C'))

        node3 = cq5._head.prev
        self.assertNodeEqual(node3, Process('C'), Process('B'), Process('A'))

    def test_remove_process_3_middle(self):
        p1 = Process('A')
        p2 = Process('B')
        p3 = Process('C')
        cq6 = CircularQueue([p1,p2,p3])

        removed_node = cq6.remove_process(p2)
        self.assertEqual(removed_node,Process('B'))
        
        self.assertEqual(len(cq6), 2)

        node1 = cq6._head
        self.assertNodeEqual(node1, Process('A'), Process('C'), Process('C'))

        node3 = cq6._head.prev
        self.assertNodeEqual(node3, Process('C'), Process('A'), Process('A'))

    def test_remove_process_3_head(self):
        p1 = Process('A')
        p2 = Process('B')
        p3 = Process('C')
        cq7 = CircularQueue([p1,p2,p3])

        removed_node = cq7.remove_process(p1)
        self.assertEqual(removed_node,Process('A'))
        
        self.assertEqual(len(cq7), 2)

        node1 = cq7._head
        self.assertNodeEqual(node1, Process('B'), Process('C'), Process('C'))

        node3 = cq7._head.prev
        self.assertNodeEqual(node3, Process('C'), Process('B'), Process('B'))

    def test_remove_process_3_final(self):
        p1 = Process('A')
        p2 = Process('B')
        p3 = Process('C')
        cq8 = CircularQueue([p1,p2,p3])

        removed_node = cq8.remove_process(p3)
        self.assertEqual(removed_node,Process('C'))

        self.assertEqual(len(cq8), 2)

        node1 = cq8._head
        self.assertNodeEqual(node1, Process('A'), Process('B'), Process('B'))

        node3 = cq8._head.prev
        self.assertNodeEqual(node3, Process('B'), Process('A'), Process('A'))

    def test_remove_process_1(self):
        p1 = Process('A')
        cq9 = CircularQueue([p1])

        removed_node = cq9.remove_process(p1)
        self.assertEqual(removed_node,Process('A'))

        self.assertEqual(len(cq9), 0)
        self.assertEqual(cq9._head, None)

    def test_kill_3_middle(self):
        p1 = Process('A')
        p2 = Process('B')
        p3 = Process('C')
        cq10 = CircularQueue([p1,p2,p3])

        killed_node = cq10.kill('B')
        self.assertEqual(killed_node,Process('B'))

        self.assertEqual(len(cq10), 2)

        node1 = cq10._head
        self.assertNodeEqual(node1, Process('A'), Process('C'), Process('C'))

        node3 = cq10._head.prev
        self.assertNodeEqual(node3, Process('C'), Process('A'), Process('A'))

    def test_repr(self):
        p1 = Process('A')
        p2 = Process('B')
        p3 = Process('C')
        cq11 = CircularQueue([p1,p2,p3])

        self.assertEqual(repr(cq11), f"CircularQueue(Process(A, 100), Process(B, 100), Process(C, 100))")

if __name__ == "__main__":
    unittest.main()
