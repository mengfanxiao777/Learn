from max_sums import MAX
from unittest import TestCase
import unittest
class TestMAX(TestCase):
    def test1_MAX(self):
        self.assertEqual(MAX([1,2,3,4],4),10)

    def test2_MAX(self):
        self.assertEqual(MAX([1,2,3,4],4),100)
        # 正确值为100
    def test3_MAX(self):
        self.assertEqual(MAX([-1,2,-3,4],4),3)
        #正确值为4
    def test4_MAX(self):
        self.assertEqual(MAX([1,-2,4,2],4),6)
if __name__ == '__main__':
	unittest.main()