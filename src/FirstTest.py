import unittest

def is_odd(n):
	return n % 2 == 1

class is_Odd_Tests(unittest.TestCase):

	def testOne(self):
		self.failUnless(is_odd(1))

	def testTwo(self):
		self.failIf(is_odd(2))

def main():
	unittest.main()

if __name__ == '__main__':
	main()