# импортируем модули random, pygame и time
import pygame
import random
import time

pygame.init() # инициализирует все модули pygame

# такие постоянные, как размер экрана (длина и ширина), несколько цветов
size = width, height = (400, 600) 
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
clock = pygame.time.Clock() # для отслеживания времени

speed = 5 # начальная скорость

screen = pygame.display.set_mode(size) # создаем экран вышеупомянутыми размерами
screen.fill(WHITE) # экран заполняем белым
pygame.display.set_caption('Racer') # добавляем название игры в верхней части экрана заголовка
font = pygame.font.SysFont("Verdana", 20) # шрифт - Verdana, размер - 20
score_text = font.render("SCORE:", True, BLACK) # Создаем текст черного цвета - "SCORE"
font1 = pygame.font.SysFont("Verdana", 60) # шрифт - Verdana, размер - 60
game_over = font1.render("GAME OVER", True, BLACK) # Создаем текст черного цвета - "GAME OVER"
background = pygame.image.load("zhol.jpg") # Загружаем картинку для фона

pygame.mixer.music.load('b.wav')
pygame.mixer.music.play()

class Enemy(pygame.sprite.Sprite): # создаем дочерний класс Enemy
    def __init__(self): # функция для инициализации
        super().__init__() # инициализируем из родительского класса
        self.image = pygame.image.load('kzlmawna.jpg') # загружаем картинку
        self.rect = self.image.get_rect() # около картинки описываем прямоугольник
        self.x = random.randint(40, 300) # начальная координата по оси Оx, выбирается рандомно из заданного интервала
        self.y = 0 # начальная координата по оси Оу
        self.rect.center = (self.x, self.y) # точка прямоугольника, ее координаты - self.x и self.y (выше описаны)
    
    def move(self): # функция для передвижения
        self.rect.move_ip(0, speed) # сдвигает прямоугольник, а вместе с ней и картинку, на 5 вниз
        self.y += speed # каждый раз к начальной координате по оси Оу добавляем 5
        if self.rect.top > 600: # проверяем, если прямоугольник выходит за границу экрана (вниз), то он возвращается наверх, координата по Оу снова равна 0, а координата по Ох снова выбирается рандомно из заданного интервала, а в противном случае продолжает свое движение вниз
            self.rect.top = 0
            self.x = random.randint(40, 300)
            self.y = 0
            self.rect.center = (self.x, self.y)
    
class Player(pygame.sprite.Sprite): # создаем дочерний класс Enemy
    def __init__(self): # функция для инициализации
        super().__init__() # инициализируем из родительского класса
        self.image = pygame.image.load('kokmawna.jpg') # загружаем картинку
        self.rect = self.image.get_rect() # около картинки описываем прямоугольник
        self.x = 160 # задаем начальную координату по Ох
        self.y = 520 # задаем начальную координату по Оу
        self.rect.center = (self.x, self.y) # точка прямоугольника, ее координаты - self.x и self.y (выше описаны)

    def move(self): # функция для передвижения
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0: # проверяем, если прямоугольник не выходит за границу экрана (влево) и нажата кнопа "Left" с клавиатуры, то он перемещается влево на 5, координата по Ох уменьшается на 5
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-5, 0)
                self.x -=5
        if self.rect.right < width: # проверяем, если прямоугольник не выходит за границу экрана (вправо) и нажата кнопа "Right" с клавиатуры, то он перемещается вправо на 5, координата по Ох увеличивается на 5
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(5, 0)
                self.x += 5

    def earn(self, coinx, coiny): # функция для зарабатывания монет, которой передаем 2 параметра, которые являются координатами центра монеты 
        if self.x - 50 <= coinx <= self.x + 50 and self.y - 50 <= coiny <= self.y + 50: # если центр монеты лежит в данном интервале, то функция возвращает значение True, в противном случае - возвращает значение False
            return True
        return False

P1 = Player() # вызываем класс Player

class Coins(pygame.sprite.Sprite): # создаем дочерний класс Coins
    def __init__(self): # функция для инициализации
        super().__init__() # инициализируем из родительского класса
        self.image = pygame.image.load('moneta.jpg') # загружаем картинку
        self.rect = self.image.get_rect() # около картинки описываем прямоугольник
        self.x = random.randint(12, 290) # начальная координата по оси Оx, выбирается рандомно из заданного интервала
        self.y = 0 # начальная координата по оси Оу
        self.rect.center = (self.x, self.y) # точка прямоугольника, ее координаты - self.x и self.y (выше описаны)
        self.score = 0 # переменная для счета 

    def move(self): # функция для передвижения
        self.rect.move_ip(0, speed) # сдвигает прямоугольник, а вместе с ней и картинку, на 5 вниз
        self.y += speed # каждый раз к начальной координате по оси Оу добавляем 5
        if self.rect.top > 600: # проверяем, если прямоугольник выходит за границу экрана (вниз), то он возвращается наверх, координата по Оу снова равна 0, а координата по Ох снова выбирается рандомно из заданного интервала
            self.rect.top = 0
            self.x = random.randint(40, 300)
            self.y = 0
            self.rect.center = (self.x, self.y)
        else: # в противном случае проверяется функция для зарабатывания монет из класса Player
            if P1.earn(self.x, self.y): # если эта функция возвращает значение True, то монета генерируется заново, а наш счетчик увеличивается на 1
                self.rect.top = 0
                self.x = random.randint(12, 290)
                self.y = 0
                self.rect.center = (self.x, self.y)
                self.score += 1

E1 = Enemy() # вызываем класс Enemy
C1 = Coins() # вызываем класс Coins
enemies = pygame.sprite.Group() # создаем группу спрайтов enemies, в которую добавляем класс Enemy
enemies.add(E1)
all_sprites = pygame.sprite.Group() # создаем группу спрайтов all_sprites, в которую добавляем класс Enemy и Player
all_sprites.add(P1)
all_sprites.add(E1)
players = pygame.sprite.Group() # создаем группу спрайтов players, в которую добавляем класс Player
players.add(P1)

INC_SPEED = pygame.USEREVENT + 1 # создаем новое событие INC_SPEED, которые происходит каждые 3 секунды 
pygame.time.set_timer(INC_SPEED, 3000)

# Игровой цикл, в котором программа продолжает цикл снова и снова, пока не произойдет событие типа QUIT
done = False
while not done:
    for event in pygame.event.get():
        if event.type == INC_SPEED: # если происходит событие INC_SPEED, то скорость увеличивается на 0.5
            speed += 0.5
        if event.type == pygame.QUIT:
            done = True
    screen.blit(background, (0,0)) # выводим на экран картинку фоновую
    screen.blit(score_text, (310, 10)) # выводим текст "SCORE" на экран, на позицию (310, 10)
    for entity in all_sprites: # каждый спрайт из группы all_sprites выводим на экран и вызываем функцию move (для передвижения)
        screen.blit(entity.image, entity.rect)
        entity.move()
    screen.blit(C1.image, C1.rect) # выводим на экран картинку с монетой
    C1.move() # вызываем функцию move из класса Coins (для передвижения монет)
    scores = font.render(str(C1.score), True, BLACK) # текст, который принимает значение счетчика
    screen.blit(scores, (340, 45)) # выводим значение счетчика на экран, на позицию (340, 45)
    pygame.draw.rect(screen, BLACK, (300, 1, 96, 80), 1) # рисуем прямоугольник черного цвета на экране (длина - 80, ширина - 96, толщина - 1, а начальные координаты - (300, 1)) для отделения текста с счетчиков от основного поля игры

    if pygame.sprite.spritecollideany(P1, enemies): # проверяем на коллизию. если коллизия была, то происходит пауза в 0.5 секунд, затем экран заливается красным, и выходит текст "GAME OVER" и "убираем" все спрайты группы all_sprites. затем снова пауза в 2 секунды, и затем происходит выход из игры
        pygame.mixer.Sound('a.wav').play() # запускаем мелодию
        time.sleep(0.5)
        screen.fill(RED)
        screen.blit(game_over, (25,250))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(2)
        pygame.quit()
        
    clock.tick(30) # вызывает 30 кадров в секунду
    pygame.display.update() # обновляем содержимое дисплея игры

pygame.quit() # отключает модуль pygame