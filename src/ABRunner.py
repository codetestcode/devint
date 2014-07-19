import unittest

def add(n1,n2):
	return n1 + n2


class AdditionTest(unittest.TestCase):

	def test_add_pos_nums(self):
		self.assertEquals(4, add(2,2))

	def test_add_zero_nums(self):
		self.assertEquals(0, add(0,0))

def subtract(n1,n2):
	return n1 - n2


class SubtractTest(unittest.TestCase):

	def test_subtract_pos_nums(self):
		self.assertEquals(0, subtract(2,2))

	def test_subtract_zero_nums(self):
		self.assertEquals(0, subtract(0,0))


if __name__ == '__main__':
	suite1 = unittest.TestLoader().loadTestsFromTestCase(AdditionTest)
	suite2 = unittest.TestLoader().loadTestsFromTestCase(SubtractTest)
	suite = unittest.TestSuite([suite1,suite2])
	unittest.TextTestRunner(verbosity=2).run(suite)