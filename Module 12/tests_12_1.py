import unittest
import random

class Runner:
	def __init__(self, name):
		self.name = name
		self.distance = 0

	def run(self):
		self.distance += 10

	def walk(self):
		self.distance += 5

	def __str__(self):
		return self.name


class RunnerTest(unittest.TestCase):
	def test_walk(self):
		self.runner = Runner('Jeremy Clarkson')
		for i in range(10):
			self.runner.walk()
		self.assertEqual(self.runner.distance, 50)

	def test_run(self):
		self.runner = Runner('James May')
		for i in range(10):
			self.runner.run()
		self.assertEqual(self.runner.distance, 100)

	def test_challenge(self):
		self.runner1 = Runner('Jeremy Clarkson')
		self.runner2 = Runner('James May')
		for i in range(10):
			if random.choice([True, False]):
				self.runner1.run()
			else:
				self.runner1.walk()
			if random.choice([True, False]):
				self.runner2.run()
			else:
				self.runner2.walk()
		self.assertNotEqual(self.runner1.distance, self.runner2.distance)


if '__name__' == '__main__':
	unittest.main()