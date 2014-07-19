import unittest

class Outcomes(unittest.TestCase):

	def testPass(self):
		return

	def testFail(self):
		self.failIf(False)

	# def testError(self):
	# 	raise RuntimeError('Test error for raise')

if __name__ == '__main__':
	unittest.main()