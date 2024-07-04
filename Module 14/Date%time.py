from datetime import datetime


class SuperDate(datetime):
    def __init__(self, *args):
        self.seasons = {'Summer': [6, 7, 8], 'Autumn':[9, 10, 11], 'Winter':[12, 1, 2], 'Spring':[3, 4, 5]}
        self.periods = {
            'Morning': [6, 7, 8, 9, 10, 11],
            'Day': [12, 13, 14, 15, 16, 17],
            'Evening': [18, 19, 20, 21, 22, 23],
            'Night': [0, 1, 2, 3, 4, 5]
        }

    def get_season(self):
        for i in self.seasons.items():
            if self.month in i[1]:
                print(i[0])

    def get_time_of_day(self):
        for i in self.periods.items():
            if self.hour in i[1]:
                print(i[0])


a = SuperDate(2024, 2, 22, 12)

a.get_season()
a.get_time_of_day()
