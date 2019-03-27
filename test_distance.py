import unittest
from distance import distance


class TestDistance(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.something = "Set Up common"
        print(cls.something)

    def setUp(self):
        self.something2 = "Set Up"
        print(self.something2)

    def test_zero_coor(self):
        number = [12, 433, 5, 0, 1]
        for num in number:
            with self.subtest(num):
                print(num)
                res = num % 2
                self.assertEqual(res, 0)

    def test_1(self):
        res = distance(0, 0, 1, 1)
        self.assertEqual(res, 2**0.5)

    def test_2(self):
        res = distance(0, 0, 3, 4)
        self.assertEqual(res, 5)


if __name__ == '__main__':
    # test1 = TestDistance("test_zero_coor")
    # test2 = TestDistance("test_1")

    # suite1 = unittest.TestSuite([test1])
    # suite1.addTest(test2)
    # result = unittest.TestResult()
    # print(result)
    # suite1 = unittest.TestLoader().loadTestsFromTestCase(TestDistance)
    # result = unittest.TestResult()
    # suite1.run(result)
    # print(result)
    from HtmlTestRunner import HTMLTestRunner
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output=r"C:\Users\Oleg Ilin\test_repo_190202\untitled9"))
