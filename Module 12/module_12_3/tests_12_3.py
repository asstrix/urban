import unittest
import random


class Runner:
	def __init__(self, name, speed=5):
		self.name = name
		self.distance = 0
		self.speed = speed

	def run(self):
		self.distance += self.speed * 2

	def walk(self):
		self.distance += self.speed

	def __str__(self):
		return self.name

	def __eq__(self, other):
		if isinstance(other, str):
			return self.name == other
		elif isinstance(other, Runner):
			return self.name == other.name


class Tournament:
	def __init__(self, distance, *participants):
		self.full_distance = distance
		self.participants = list(participants)

	def start(self):
		finishers = {}
		place = 1
		while self.participants:
			finished_participants = []
			for participant in self.participants:
				participant.run()
				if participant.distance >= self.full_distance:
					finishers[place] = participant
					place += 1
					finished_participants.append(participant)
			for participant in finished_participants:
				self.participants.remove(participant)
		return finishers


class TournamentTest(unittest.TestCase):
	all_results = {}
	is_frozen = True

	@unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
	def tearDown(self):
		print(self.all_results)

	@unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
	def setUp(self):
		self.r1 = Runner('Усэйн', 10)
		self.r2 = Runner('Андрей', 9)
		self.r3 = Runner('Ник', 3)

	@unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
	def test_1(self):
		trnmt = Tournament(90, self.r1, self.r3)
		self.all_results.update({key: value.name for key, value in trnmt.start().items()})
		last_key = next(reversed(self.all_results))
		self.assertEqual(self.all_results[last_key], 'Ник')

	@unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
	def test_2(self):
		trnmt = Tournament(90, self.r2, self.r3)
		self.__class__.all_results = {key: value.name for key, value in trnmt.start().items()}
		last_key = next(reversed(self.all_results))
		self.assertEqual(self.all_results[last_key], 'Ник')

	@unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
	def test_3(self):
		trnmt = Tournament(90, self.r1, self.r2, self.r3)
		self.__class__.all_results = {key: value.name for key, value in trnmt.start().items()}
		last_key = next(reversed(self.all_results))
		self.assertEqual(self.all_results[last_key], 'Ник')


class RunnerTest(unittest.TestCase):
	is_frozen = False

	@unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
	def test_walk(self):
		self.runner = Runner('Jeremy Clarkson')
		for i in range(10):
			self.runner.walk()
		self.assertEqual(self.runner.distance, 50)

	@unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
	def test_run(self):
		self.runner = Runner('James May')
		for i in range(10):
			self.runner.run()
		self.assertEqual(self.runner.distance, 100)

	@unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
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

