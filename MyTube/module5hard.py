import time

class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return f'{self.nickname}'


class Video:

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title

    def __repr__(self):
        return f'{self.title}'


class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user
                print(f'Вы вошли как {self.current_user.nickname}')
                return
        print('Неверный никнейм или пароль')

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь с никнеймом {nickname} уже существует')
                return
        new_user = User(nickname, hash(password), age)
        self.users.append(new_user)
        print(f'Пользователь {nickname} успешно зарегистрирован')
        self.log_in(nickname, hash(password))

    def log_out(self):
        self.current_user = None
        return print('Вы вышли')

    def add(self, *args):
        args = list(args)
        for video in args:
            if video not in self.videos:
                self.videos.append(video)
                print(f'Видео "{video.title}" добавлено')

    def get_videos(self, keyword):
        video_list = []
        for video in self.videos:
            if keyword.lower() in video.title.lower():
                video_list.append(video.title)
        return video_list

    def __str__(self):
        video_titles = []
        user_base = []
        for video in self.videos:
            video_titles.append(video.title)
        for user in self.users:
            user_base.append(user.nickname)
        return f'ЧТО-НИБУДЬ ПОЛЕЗНОЕ ВЕРНЕТ КОГДА-НИБУДЬ'

    def watch_video(self, video_title):
        video_found = False
        if self.current_user is None:
            return print(f'Войдите в аккаунт, чтобы смотреть видео')
        for video in self.videos:
            if video_title == video.title:
                video_found = True
                if video.adult_mode and self.current_user.age < 18:
                    return print('Вам нет 18 лет, пожалуйста покиньте страницу')
                while video.time_now <= video.duration:
                    print(f'Вы смотрите видео "{video.title}" {video.time_now} секунд')
                    time.sleep(1)
                    video.time_now += 1
                print(f'Конец видео "{video.title}"')
                video.time_now = 0
                return
        if not video_found:
            print(f'Видео "{video_title}" не найдено')



ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# # Проверка поиска
# print(ur)
# print(repr(v1))
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
# # Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
# ur.log_out()
ur.watch_video('Для чего девушкам парень программист?')
# print(ur.videos)
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# # Проверка входа в другой аккаунт
# ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
# print(ur.current_user)
# print(ur.users[0].password)
# # Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программироssвания 2024 года!')
