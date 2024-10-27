from time import sleep
class User:
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
    def __str__(self):
        return self.nickname
class Video:
    def __init__(self, title: str, duration: int, adult_mode = False):
        self.title = title #заголовок
        self.duration = duration # продолжительность
        self.time_now = 0
        self.adult_mode = adult_mode
class UrTube(User):
    def __init__(self):
        self.users = list() #спсиок объектов класса User
        self.videos = list() #список объектов класса Video
        self.current_user = None # текущий пользователь
    def log_in (self, nickname, password):
        for user in self.users:
            if nickname == user.nickname and hash(password) == user.password:
                self.current_user = user
                print(f'Добро пожаловать, {nickname}')
                break
        else:
            print("Данного пользователя не существует")
    def register(self, nickname, password, age):
        if self.users == list():
            self.users.append(User(nickname, password, age))
            print('Вы успешно зарегистрировались. Вход выполнен автоматически. Приятного пользования!')
            self.current_user = self.users[0]
            return
        for user in self.users:
            if nickname in user.nickname:
                print(f"Пользователь {nickname} уже существует")
                break
            else:
                self.users.append(User(nickname,password,age))
                print('Вы успешно зарегистрировались. Вход выполнен автоматически. Приятного пользования!')
                self.current_user = (User(nickname, password, age))
                break
    def log_out(self):
        print(f'До свидания, {self.current_user.nickname}')
        self.current_user = None
    def add(self, *args):
        args = list(args)
        for downloading_video in args:
            is_true = False
            if self.videos == list():
                self.videos.append(downloading_video)
                print(f'Вы успешно загрузили видео "{downloading_video.title}" на свой канал')
                continue
            for video in self.videos:
                if  downloading_video.title == video.title:
                    print('Нельзя загрузить видео с одинаковыми названиями')
                    is_true = True
                    break
            if is_true == False:
                self.videos.append(downloading_video)
                print(f'Вы успешно загрузили видео "{downloading_video.title}" на свой канал')
    def get_videos(self, searching: str):
        find_video = list()
        for video in self.videos:
            if searching.upper() in video.title.upper():
                find_video.append(video.title)
        return find_video
    def watch_video(self, entering_video):
        """
        Метод watch_video, который принимает название фильма, если не находит точного совпадения
        (вплоть до пробела), то ничего не воспроизводится, если же находит - ведётся отчёт в консоль на какой
         секунде ведётся просмотр. После текущее время просмотра данного видео сбрасывается.
        """
        for video in self.videos:
            if entering_video == video.title: #если видео найдено, то:
                if video.adult_mode == True: # если возрастное ограничение есть, то:
                    if self.current_user == None: # если вход в профиль не выполнен, то
                        print("Войдите в аккаунт, чтобы смотреть видео")
                    elif self.current_user.age >= 18: # иначе, если текущий пользователь старше 18 лет
                        for time in range(1,video.duration+1):
                            video.time_now = time
                            print(time, end = ' ')
                            sleep(1)
                        print('Конец')
                    elif self.current_user.age < 18:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")




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
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
