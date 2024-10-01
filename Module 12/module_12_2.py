from unittest import TestCase, main


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


class TournamentTest(TestCase):
    all_results = {}

    def tearDown(self):
        print(self.all_results)

    def setUp(self):
        self.r1 = Runner('Усэйн', 10)
        self.r2 = Runner('Андрей', 9)
        self.r3 = Runner('Ник', 3)

    def test_1(self):
        trnmt = Tournament(90, self.r1, self.r3)
        self.all_results.update({key: value.name for key, value in trnmt.start().items()})
        last_key = next(reversed(self.all_results))
        self.assertEqual(self.all_results[last_key], 'Ник')

    def test_2(self):
        trnmt = Tournament(90, self.r2, self.r3)
        self.__class__.all_results = {key: value.name for key, value in trnmt.start().items()}
        last_key = next(reversed(self.all_results))
        self.assertEqual(self.all_results[last_key], 'Ник')

    def test_3(self):
        trnmt = Tournament(90, self.r1, self.r2, self.r3)
        self.__class__.all_results = {key: value.name for key, value in trnmt.start().items()}
        last_key = next(reversed(self.all_results))
        self.assertEqual(self.all_results[last_key], 'Ник')


if '__name__' == '__main__':
    main()
