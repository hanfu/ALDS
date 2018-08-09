from sorting import HeapSort
#need to parameterize testing funcs
import unittest
import random

class Test(unittest.TestCase):
	def test_single(self):
		arr = [1]
		HeapSort(arr)
		self.assertEqual([1], arr)
	def test_nodup(self):
		arr = random.sample(range(10),k=5)
		arr_test = arr[:]
		self.assertEqual(HeapSort(arr_test), arr.sort())
	def test_withdup(self):
		arr = random.choices(range(10),k=10)
		arr_test = arr[:]
		self.assertEqual(HeapSort(arr_test), arr.sort())


if __name__ == '__main__':
	unittest.main()