import unittest
from version.main import compare_versions


class Compare(unittest.TestCase):

    def test_b_bigger1(self):
        a = 1.0
        b = 2.1
        self.assertEqual(compare_versions(a, b), -1)

    def test_b_bigger2(self):
        a = "1.0"
        b = "2.1.3"
        self.assertEqual(compare_versions(a, b), -1)

    def test_b_bigger3(self):
        a = 1
        b = "2.1.3"
        self.assertEqual(compare_versions(a, b), -1)

    def test_b_bigger3(self):
        a = "2.1.3.1"
        b = "2.1.3.2"
        self.assertEqual(compare_versions(a, b), -1)

    def test_b_bigger4(self):
        a = "2.1"
        b = "2.1.3.2"
        self.assertEqual(compare_versions(a, b), -1)

    def test_b_bigger5(self):
        a = "1155.7.8.4.2.35.2.2"
        b = "1205.1.3.2"
        self.assertEqual(compare_versions(a, b), -1)

    def test_a_bigger1(self):
        a = 3.0
        b = 2.1
        self.assertEqual(compare_versions(a, b), 1)

    def test_a_bigger2(self):
        a = "3.0"
        b = "2.1.3"
        self.assertEqual(compare_versions(a, b), 1)

    def test_a_bigger3(self):
        a = 6
        b = "2.1.3"
        self.assertEqual(compare_versions(a, b), 1)

    def test_a_bigger3(self):
        a = "2.1.3.3"
        b = "2.1.3.2"
        self.assertEqual(compare_versions(a, b), 1)

    def test_a_bigger4(self):
        a = "2.1.4.1"
        b = "2.1.3.2"
        self.assertEqual(compare_versions(a, b), 1)

    def test_a_bigger5(self):
        a = "5155.7.8.4.2.35.2.2"
        b = "1205.1.3.2"
        self.assertEqual(compare_versions(a, b), 1)

    def test_a_bigger6(self):
        a = "1.2.a"
        b = "1.2.9"
        self.assertEqual(compare_versions(a, b), 1)

    def test_equal1(self):
        a = "2"
        b = "2"
        self.assertEqual(compare_versions(a, b), 0)

    def test_equal2(self):
        a = 3.1
        b = 3.1
        self.assertEqual(compare_versions(a, b), 0)

    def test_equal3(self):
        a = "2.0.1"
        b = "2.0.1"
        self.assertEqual(compare_versions(a, b), 0)

    def test_equal4(self):
        a = "5.0.1.9c"
        b = "5.0.1.9c"
        self.assertEqual(compare_versions(a, b), 0)

    def test_equal5(self):
        a = "5.0.a.9"
        b = "5.0.a.9"
        self.assertEqual(compare_versions(a, b), 0)

if __name__ == '__main__':
    unittest.main()
