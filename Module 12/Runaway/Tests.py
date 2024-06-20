import unittest
from main import Student


class SelfTest(unittest.TestCase):
    def setUp(self):
        self.students = [Student('Jeremy Clarkson'), Student('James May'), Student('Richard Hammond')]

    def test_walk(self):
        for i in range(10):
            self.students[0].walk()
        self.assertLess(self.students[0].distance, 500)
        print(f'Distances are not equal [distance of {self.students[0].name}]!=500')

    def test_run(self):
        for i in range(10):
            self.students[1].run()
        self.assertLess(self.students[1].distance, 1000)
        print(f'Distances are not equal [distance of {self.students[1].name}]!=500')

    def test_run_and_walk(self):
        for i in range(10):
            self.students[1].run()
            self.students[0].walk()
        self.assertLess(self.students[0].distance - self.students[1].distance, 0)
        print(f'[Running {self.students[1].name}] overcame a distance more than [Walking {self.students[0].name}]')


if '__name__' == '__main__':
    unittest.main()
