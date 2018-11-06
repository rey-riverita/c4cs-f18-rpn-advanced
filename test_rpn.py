import unittest
import rpn

class TestBasics(unittest.TestCase):
	def test_add(self):
		result = rpn.calculate("1 1 +")
		self.assertEqual(2, result)
	
	def test_sub(self):
		result = rpn.calculate("4 3 -")
		self.assertEqual(1, result)
	
	def test_mult(self):
		result = rpn.calculate("2 3 *")
		self.assertEqual(6, result)

	def test_div(self):
		result = rpn.calculate("10 2 /")
		self.assertEqual(5, result)

	def test_exp(self):
		result = rpn.calculate("5 2 ^")
		self.assertEqual(25, result)


# TODO: add a test for subtract