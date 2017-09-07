import unittest
import SortedSearch as ss
import numpy as np

arr  = np.array([1,2,3,4,5,5,6,7]) 
rarr = np.flipud(arr).copy() # [7,6,5,5,4,3,2,1]

class TestIndex(unittest.TestCase):
    def test_nodup(self):
        val = 3
        i = ss.index(arr, val)
        self.assertEqual(i, 2)
    def test_dup(self):
        val = 5
        i = ss.index(arr, val)
        self.assertEqual(i, 4)
    def test_none(self):
        val = 1.2
        self.assertRaises(ValueError, ss.index, arr, val)

    def test_rnodup(self):
        val = 3
        i = ss.index(rarr, val, reverse=True)
        self.assertEqual(i, 5)
    def test_rdup(self):
        val = 5
        i = ss.index(rarr, val, reverse=True)
        self.assertEqual(i, 3)
    def test_rnone(self):
        val = 1.2
        self.assertRaises(ValueError, ss.index, rarr, val, reverse=True)

class Testlt(unittest.TestCase):
    def test_lowend(self):
        self.assertRaises(ValueError, ss.find_lt, arr, 0)
    def test_highend(self):
        i,v = ss.find_lt(arr, 10)
        self.assertEqual(i, 7)
        self.assertEqual(v, 7)
    def test_middle_ne(self):
        i,v = ss.find_lt(arr, 5.5)
        self.assertEqual(i, 5)
        self.assertEqual(v, 5)
    def test_middle_eq(self):
        i,v = ss.find_lt(arr, 5)
        self.assertEqual(i, 3)
        self.assertEqual(v, 4)

    def test_rlowend(self):
        self.assertRaises(ValueError, ss.find_lt, rarr, 0, reverse=True)
    def test_rhighend(self):
        i,v = ss.find_lt(rarr, 10, reverse=True)
        self.assertEqual(i, 0)
        self.assertEqual(v, 7)
    def test_rmiddle_ne(self):
        i,v = ss.find_lt(rarr, 5.5, reverse=True)
        self.assertEqual(i, 2)
        self.assertEqual(v, 5)
    def test_rmiddle_eq(self):
        i,v = ss.find_lt(rarr, 5, reverse=True)
        self.assertEqual(i, 4)
        self.assertEqual(v, 4)

class Testgt(unittest.TestCase):
    def test_lowend(self):
        i,v = ss.find_gt(arr, 0)
        self.assertEqual(i, 0)
        self.assertEqual(v, 1)
    def test_highend(self):
        self.assertRaises(ValueError, ss.find_gt, arr, 10)
    def test_middle_ne(self):
        i,v = ss.find_gt(arr, 4.5)
        self.assertEqual(i, 4)
        self.assertEqual(v, 5)
    def test_middle_eq(self):
        i,v = ss.find_gt(arr, 5)
        self.assertEqual(i, 6)
        self.assertEqual(v, 6)

    def test_rlowend(self):
        i,v = ss.find_gt(rarr, 0, reverse=True)
        self.assertEqual(i, 7)
        self.assertEqual(v, 1)
    def test_rhighend(self):
        self.assertRaises(ValueError, ss.find_gt, rarr, 10, reverse=True)
    def test_rmiddle_ne(self):
        i,v = ss.find_gt(rarr, 4.5, reverse=True)
        self.assertEqual(i, 3)
        self.assertEqual(v, 5)
    def test_rmiddle_eq(self):
        i,v = ss.find_gt(rarr, 5, reverse=True)
        self.assertEqual(i, 1)
        self.assertEqual(v, 6)

class Testge(unittest.TestCase):
    def test_lowend(self):
        i,v = ss.find_ge(arr, 0)
        self.assertEqual(i, 0)
        self.assertEqual(v, 1)
    def test_highend(self):
        self.assertRaises(ValueError, ss.find_ge, arr, 10)
    def test_middle_ne(self):
        i,v = ss.find_ge(arr, 4.5)
        self.assertEqual(i, 4)
        self.assertEqual(v, 5)
    def test_middle_eq(self):
        i,v = ss.find_ge(arr, 5)
        self.assertEqual(i, 4)
        self.assertEqual(v, 5)

    def test_rlowend(self):
        i,v = ss.find_ge(rarr, 0, reverse=True)
        self.assertEqual(i, 7)
        self.assertEqual(v, 1)
    def test_rhighend(self):
        self.assertRaises(ValueError, ss.find_ge, rarr, 10, reverse=True)
    def test_rmiddle_ne(self):
        i,v = ss.find_ge(rarr, 4.5, reverse=True)
        self.assertEqual(i, 3)
        self.assertEqual(v, 5)
    def test_rmiddle_eq(self):
        i,v = ss.find_ge(rarr, 5, reverse=True)
        self.assertEqual(i, 3)
        self.assertEqual(v, 5)

class Testle(unittest.TestCase):
    def test_lowend(self):
        self.assertRaises(ValueError, ss.find_le, arr, 0)
    def test_highend(self):
        i,v = ss.find_le(arr, 10)
        self.assertEqual(i, 7)
        self.assertEqual(v, 7)
    def test_middle_ne(self):
        i,v = ss.find_le(arr, 5.5)
        self.assertEqual(i, 5)
        self.assertEqual(v, 5)
    def test_middle_eq(self):
        i,v = ss.find_le(arr, 5)
        self.assertEqual(i, 5)
        self.assertEqual(v, 5)

    def test_rlowend(self):
        self.assertRaises(ValueError, ss.find_le, rarr, 0, reverse=True)
    def test_rhighend(self):
        i,v = ss.find_le(rarr, 10, reverse=True)
        self.assertEqual(i, 0)
        self.assertEqual(v, 7)
    def test_rmiddle_ne(self):
        i,v = ss.find_le(rarr, 5.5, reverse=True)
        self.assertEqual(i, 2)
        self.assertEqual(v, 5)
    def test_rmiddle_eq(self):
        i,v = ss.find_le(rarr, 5, reverse=True)
        self.assertEqual(i, 2)
        self.assertEqual(v, 5)

if __name__ == '__main__':
    unittest.main()

        

