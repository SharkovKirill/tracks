import time
class Track():
    def __init__(self, name, duration, author, year):
        self.name = name
        self.duration = int(duration)
        self.author = author
        self.year = year
        self.current = 0
        self.play = False
        self.repeat = False

    def pause(self, choice=0):
        if self.repeat == True:
            self.current = (int(self.current) + int(time.time()) - int(self.o_time))% self.current
            print('Трек поставлен на паузу')
        elif self.repeat == False:
            if self.play ==True:
                if (int(self.current) + int(time.time()) - int(self.o_time))<self.duration:
                    self.play = False
                    self.current = self.current + int(time.time()) - int(self.o_time)
                    if choice==0:
                        print(f'Трек {self.name} поставлен на паузу')
                else:
                    print('Невозможно поставить трек на паузу')
            else:
                print('Невозможно поставить трек на паузу')

    def start(self):
        if self.play == True:
            print('Ошибка. Трек уже воспроизводится')

        else:
            self.play = True
            print('C', self.current,'секунды поставлен на воспроизведение:', self.name)
            self.o_time = time.time()


    def stop(self):
        self.play = False
        self.current = 0

    def on_repeat(self):
        print('Повторение включено')
        self.repeat = True
    def off_repeat(self):
        print('Повторение выключено')
        self.repeat = False


class Album():
    def __init__(self, album_name, year, author):
        self.tracks = []
        self.album_name = album_name
        self.year = year
        self.author = author

    def add_track(self, track):
        self.tracks.append(track)

    def sum_duration(self):
        s = 0
        for dur in self.tracks:
            s += dur.duration
        return s
    def start(self, number):
        for track in self.tracks:
            if track.play==True and track.name!=self.tracks[number-1].name:
                print(f'Ошибка. Уже воспроизводится трек: {track.name}')
                return ask()
        return self.tracks[number - 1].start()
    def pause(self,number):
        return self.tracks[number - 1].pause()
    def stop(self,number):
        return self.tracks[number - 1].stop()

with open('input.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    line_for_album = lines[0].split(';')
    name = line_for_album.pop(2)
    album1 = Album(*line_for_album,name[:-1])
    lines.pop(0)

    for line in lines:
        line_for_track = line.split(';')
        year = line_for_track.pop(3)

        album1.add_track(Track(*line_for_track,year[:-1]))


def ask():
    while True:
        choice = input("1. Воспроизвести трек № (1 + номер трека через пробел) \n"
                      "2. Поставить трек на паузу № (2 + номер трека через пробел)\n"
                      "3. Остановить трек №(3 + номер трека через пробел)\n"
                      "4. Узнать статус  №(4 + номер трека через пробел)\n"
                      "5. Включить повтор трека №(5 + номер трека через пробел)\n"
                      "6. Выключить повтор трека №(6 + номер трека через пробел)\n")
        try:
            if 0<int(choice.split(' ')[0])<8:
                first = int(choice.split(' ')[0])
                second = int(choice.split(' ')[1])
                if first == 1:
                    album1.start(second)
                    return ask()
                if first == 2:
                    album1.pause(second)
                    return ask()
                if first == 3:
                    album1.stop(second)
                    return ask()
                if first == 4:
                    if album1.tracks[second-1].play==True:

                        album1.tracks[second - 1].pause()
                        print(f'Трек воспроизводится с {str(album1.tracks[second-1].current)} секунды')
                        album1.tracks[second - 1].start()

                    else:
                        if album1.tracks[second-1].current!=0:
                            print(f'Трек на паузе с {str(album1.tracks[second-1].current)} секунды')

                        else:
                            print('Трек не воспроизводится')

                    return ask()
            else:
                raise ValueError
        except:
            print('%s не является верным значением. Пожалуйста повторите попытку(например 1 1)' % choice)
            ask()
ask()
