# Импортируем модули random, pygame и math
import random
import pygame
import math

# Создаем функцию main, где описан весь ход работы paint
def main():
    screen = pygame.display.set_mode((800, 600)) # Создаем экран, шириной 800 и высотой 600
    screen.fill((0, 0, 0)) # Экран заполняем черным цветом
    pygame.display.set_caption('Paint') # добавляем название игры в верхней части экрана заголовка
    work_surf = pygame.Surface((800, 600)) # Создаем дополнительно surface для промежуточной отрисовки фигур
    mode = 'random' # Создаем переменную для типа выбора цвета (рандомно или нет)
    draw_on = False # Создаем переменную для отрисовки фигур
    last_pos = (0, 0) # tuple для определения начальных координат точки
    color = (255, 128, 0) # Начальный цвет
    radius = 1 # Толщина линии
    figure = 'pen' # Переменная для определения фигуры. По умолчанию - кисточка, для отрисовки линий
    # Цвета
    colors = {
        'red': (255, 0, 0),
        'blue': (0, 0, 255),
        'green': (0, 255, 0)
    }

    def Rect_pos(x1, y1, x2, y2):  # Функция для определения координат, длины и ширины прямоугольника
        return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2)) 

    # Игровой цикл, в котором программа продолжает цикл снова и снова, пока не произойдет событие типа QUIT
    done = False
    while not done:
        pressed = pygame.key.get_pressed()
        # alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        # ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN: # если нажали какую-то клавишу клавиатуры
                # if event.key == pygame.K_w and ctrl_held:
                #     pass
                # if event.key == pygame.K_F4 and alt_held:
                #     pass
                if event.key == pygame.K_1: # если нажали 1, то цвет будет красным
                    mode = 'red'
                if event.key == pygame.K_2: # если нажали 2, то цвет будет синим
                    mode = 'blue'
                if event.key == pygame.K_3: # если нажали 3, то цвет будет зеленым
                    mode = 'green'
                if event.key == pygame.K_r: # если нажали R, то фигура - прямоугольник
                    figure = 'rectangle'
                if event.key == pygame.K_p: # если нажали P, то используем кисточку, фигура - линия
                    figure = 'pen'
                if event.key == pygame.K_e: # если нажали E, то используем ластик
                    figure = 'erase'
                if event.key == pygame.K_c: # если нажали C, то фигура - круг
                    figure = 'circle'
            if event.type == pygame.MOUSEBUTTONDOWN: # если зажали левую кнопку мышки, то цвет выбирается рандомно, а в противном случае выбирается из вышеупомянутых трех цветов
                if mode == 'random':
                    color = (random.randrange(256), random.randrange(256), random.randrange(256))
                else:
                    color = colors[mode]
                draw_on = True # также, если зажали левую кнопку мышки, то переменная для отрисовки фигур меняет свое значение на true и переменная для определения конечных координат становится равной tuple для определения начальных координат точки
                last_pos = event.pos
            if event.type == pygame.MOUSEBUTTONUP: # если отпустили левую кнопку мыши, то переменная для отрисовки фигур снова меняет свое значение и выводим наш surface на экран
                work_surf.blit(screen, (0, 0))
                draw_on = False
            if event.type == pygame.MOUSEMOTION: # если мы двигаем мышкой, и переменная для отрисовки фигур = true, то мы проверяем, чем является фигура
                if draw_on:
                    if figure == 'pen': # если используем ручку, то рисуем линию на экране заданным цветом, от начальных координат до конечных, толщина - radius = 1
                        pygame.draw.line(screen, color, last_pos, event.pos, radius)
                        last_pos = event.pos # приравниваем начальные координаты к конечным, чтобы точка постоянно обновлялась
                    if figure == 'erase': # если используем ластик, то рисуем черный круг на экране, центр - конечные координаты, а радиус равен 6
                        pygame.draw.circle(screen, (0, 0, 0), (event.pos[0], event.pos[1]), 6)
                    if figure == 'rectangle': # если фигура - прямоугольник, то обращаемся к функции Rect_pos, которой передаем начальные и конечные координаты, затем выводим наш surface на экран и наконец рисуем прямоугольник на экране заданным цветом согласно функции Rect_pos
                        t = Rect_pos(last_pos[0], last_pos[1], event.pos[0], event.pos[1])
                        screen.blit(work_surf, (0, 0))
                        pygame.draw.rect(screen, color, pygame.Rect(t))
                    if figure == 'circle': # если фигура - круг, то сначала выводим наш surface на экран, а затем рисуем круг на экране заданным цветом, центр - начальные координаты, радиус - расстояния между конечными и начальными координатами (формула расстояния между двумя точками)
                        screen.blit(work_surf, (0, 0))
                        pygame.draw.circle(screen, color, (last_pos[0], last_pos[1]), int(math.sqrt((event.pos[0]-last_pos[0])**2 + (event.pos[1]-last_pos[1])**2)))

        pygame.display.flip() # обновляем содержимое дисплея игры

    pygame.quit() # отключает модуль pygame

main() # вызываем функцию main