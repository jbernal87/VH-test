import unittest
from overlap import is_overlapped


def return_false():
    return False

class TestOverlap(unittest.TestCase):

    def test_no_overlap_negative(self):
        line1 = (-1, -3)
        line2 = (-5, -9)
        #result =
        self.assertFalse(is_overlapped(line1, line2))
        pass

    def test_no_overlap_positive(self):
        line1 = (1, 3)
        line2 = (5, 7.7)
        self.assertFalse(is_overlapped(line1, line2), False)
        pass

    def test_no_overlap_mixed(self):
        line1 = (-1.677, 3.999)
        line2 = (4.01, 7.88)
        self.assertFalse(is_overlapped(line1, line2), False)

    def test_overlap_mixed(self):
        line1 = (-1.677, 3.999)
        line2 = (-4.01, 7.88)
        self.assertTrue(is_overlapped(line1, line2))

    def test_overlap_mixed2(self):
        line1 = (-1.677, -3.999)
        line2 = (-2.11, 7.88)
        self.assertTrue(is_overlapped(line1, line2))

    def test_overlap_positive(self):
        line1 = (1.677, 3.999)
        line2 = (3.991, 5.887)
        self.assertTrue(is_overlapped(line1, line2))

    def test_overlap_negative(self):
        line1 = (-11.677, -13.999)
        line2 = (-12.991, -15.887)
        self.assertTrue(is_overlapped(line1, line2))


if __name__ == '__main__':
    unittest.main()
