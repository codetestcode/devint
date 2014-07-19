import unittest

class SimplisticTest(unittest.TestCase):
	"""Simplictic test"""
	def test(self):
		self.failUnless(True)

if __name__ == '__main__':
	unittest.main()