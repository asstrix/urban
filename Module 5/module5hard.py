from time import sleep


class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


class Video:

    def __init__(self, title='', duration=0, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:

    def __init__(self):
        self.users = {}
        self.videos = {}
        self.current_user = None

    def log_in(self, login, password):
        if login in self.users and self.users[login][0] == hash(password):
            self.current_user = login
            print(f'{login} Successfully logged in')
        else:
            print('Invalid login or password')

    def register(self, nickname, password, age):
        if nickname in self.users:
            print(f'User {nickname} already exists.')
            return
        user = User(nickname, password, age)
        self.users[nickname] = [user.password, user.age]
        print(f"User '{nickname}' successfully registered.")

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            self.videos[video.title] = [video.duration, video.time_now, video.adult_mode]

    def get_videos(self, search):
        return [i for i in self.videos if search.lower() in i.lower()]

    def watch_video(self, video):
        duration = 0
        if self.current_user is not None:
            if video.lstrip(' ') in self.get_videos(video):
                if self.videos[video][2] is True and self.users[self.current_user][1] > 18:
                    for i in range(self.videos[video][0]):
                        duration += 1
                        sleep(1)
                        print(duration, end=' ')
                    print('End of video')
                else:
                    print('You are under 18 years old, please leave the page')

            else:
                print(f'{video} not found')
        else:
            print('Sign in to account')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.log_in('vasya_pupkin', 'lolkekcheburek')
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.log_in('urban_pythonist', 'iScX4vIJClb9YQavjAgF')
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')