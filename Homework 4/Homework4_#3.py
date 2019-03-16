import unittest
from leapYear import is_year_leap
from triangle import is_triangle_exist
from triangle import triangle_type


class TestYear(unittest.TestCase):

    def test_2000(self):
        res = is_year_leap(2000)
        self.assertEqual(res, True)

    def test_1900(self):
        res = is_year_leap(1900)
        self.assertEqual(res, False)

    def test_2004(self):
        res = is_year_leap(2004)
        self.assertEqual(res, True)


class TestTriangle(unittest.TestCase):

    def test_0_0_0(self):
        res = is_triangle_exist(0, 0, 0)
        self.assertEqual(res, False)

    def test_2_1_1(self):
        res = is_triangle_exist(2, 1, 1)
        self.assertEqual(res, False)

    def test_1_1_1(self):
        res = is_triangle_exist(1, 1, 1)
        self.assertEqual(res, True)

    def test_not_triangle(self):
        res = triangle_type(0, 0, 0)
        self.assertEqual(res, 'Not a triangle')

    def test_Isosceles(self):
        res = triangle_type(5, 5, 4)
        self.assertEqual(res, 'Isosceles triangle')

    def test_Equilateral(self):
        res = triangle_type(6, 6, 6)
        self.assertEqual(res, 'Equilateral triangle')

    def test_Versatile(self):
        res = triangle_type(34, 23, 12)
        self.assertEqual(res, 'Versatile triangle')


if __name__ == '__main__':
    unittest.main()
