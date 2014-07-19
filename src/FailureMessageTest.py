import unittest

class FailureMessageTest(unittest.TestCase):

	def testFail(self):
		self.failIf(False,' Testing Failure')

if __name__ == '__main__':
	unittest.main()