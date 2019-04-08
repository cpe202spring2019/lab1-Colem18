import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        self.assertEqual(max_list_iter([]),None)
        self.assertEqual(max_list_iter([2,5,1,4,7,3,2,8,0]),8)

    def test_reverse_rec(self):
        tlist = None
        with self.assertRaises(ValueError):
            reverse_rec(tlist)
        self.assertEqual(reverse_rec([2,4,6,8,10]),[10,8,6,4,2])
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])

    def test_bin_search(self):
        with self.assertRaises(ValueError):
            bin_search(2,0,7,None)
        list1 = [7,12,16,23,28,30,35,43,49,59,61]
        self.assertEqual(bin_search(14,0,len(list1)-1,list1),None)
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )

if __name__ == "__main__":
        unittest.main()

    
