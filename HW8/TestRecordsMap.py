# Import what you need
# Include unittests here. Focus on readability, including comments and docstrings.
import unittest
from RecordsMap import LocalRecord
from RecordsMap import RecordsMap
from random import randint

class TestLocalRecord(unittest.TestCase):
    def test_init(self):
        """Tests initialization of LocalRecord objects"""
        l1 = LocalRecord((41.4246,83.6446),25,75)
        
        self.assertEqual(l1.pos,(41,84))
        self.assertEqual(l1.max, 75)
        self.assertEqual(l1.min,25)


    def test_hash(self):
        """Tests hashing of LocalRecord"""

        t1 = (41, 84)
        l1 = LocalRecord(t1, 25,75)

        self.assertEqual(hash(l1), hash(t1))
        


    def test_eq(self):
        """Tests __eq__ overwrite of LocalRecord"""
        l1 = LocalRecord((41.4246,83.6446),25,75)
        l2 = LocalRecord((40.7934, 84.1446),25,75)

        self.assertEqual(l1,l2)

    def test_add_report(self):
        """Tests add_report works as intended"""

        l1 = LocalRecord((41.4246,83.6446),25,75)
        l1.add_report(80)

        self.assertEqual(l1.max,80)
        self.assertEqual(l1.min,25)

        l2 = LocalRecord((41.4246,83.6446),25,75)
        l2.add_report(20)

        self.assertEqual(l2.min,20)
        self.assertEqual(l2.max,75)

        l3 = LocalRecord((41.4246,83.6446),25,75)
        l3.add_report(50)

        self.assertEqual(l3.max,75)
        self.assertEqual(l3.min,25)

class TestRecordsMap(unittest.TestCase):
    def test_add_one_report(self):
        """Tests RecordsMap for adding one object"""
        r1 = RecordsMap()
        p1 = (41.2331,83.3332)
        r1.add_report(p1,50)

        self.assertEqual(len(r1),1)
        self.assertEqual(r1[p1], (50,50))
        self.assertTrue(p1 in r1)

        r1.add_report(p1, 55)

        self.assertEqual(len(r1), 1)
        self.assertEqual(r1[p1],(50,55))

    def test_add_many_reports(self):
        """Tests RecordsMap for adding multiple objects"""
        posList = []
        tempList = []

        for i in range(100):
            
            val = randint(0,90)     #This sections guarantees that there are some duplicates in the lists
            pos = (val,val)         #so that the following tests can make no duplicates are added to the RecordsMap
            
            temp  = val        #For the sake of later tests this is set the same value so min/max aren't changed with duplicate additions

            posList.append(pos)
            tempList.append(temp)
        
        rm = RecordsMap()

        for i in range(100):
            rm.add_report(posList[i],tempList[i])
            self.assertEqual(rm[posList[i]], (tempList[i],tempList[i]))    #Checks that correct tuple is returned for 
                                                                        #each item in RecordsMap
            self.assertTrue(posList[i] in rm)
            

        self.assertEqual(len(rm),len(set(posList))) #There shouldn't be any duplicate positions in the RecordsMap
                                                    #so it should be the same length compared to a set of the same positions
    







if __name__ == "__main__":
    unittest.main()
