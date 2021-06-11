#Подключаем библиотеки 

import pygame
import time
import random

# Создаем поле игры змейка

pygame.init()

#Цвета внашей игре

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
orange = (255, 165, 0)

width, height = 600, 400

game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Suvorov Alexandr Snake Game")

clock = pygame.time.Clock()

snake_size = 10
snake_speed = 10

message_font = pygame.font.SysFont('ubuntu', 30)
score_font = pygame.font.SysFont('ubuntu', 25)

# Эта функция счета очков, показывает где будет находится счетчики как он будет записываться 

def print_score(score):
    text = score_font.render("Score: " + str(score), True, orange)
    game_display.blit(text, [0,0])

def draw_snake(snake_size, snake_pixels):
    for pixel in snake_pixels:
        pygame.draw.rect(game_display, white, [pixel[0], pixel[1], snake_size, snake_size])


    #Эта функция отвечает за саму игру, в ней мы прописываем положение змейки и что делать если игра закончена иди вы вышли из преложения 
    #Так же отвечает за длину и размер змеки когда она будет есть и как она будет расти

def run_game():
    game_over = False
    game_close = False

    x = width / 2
    y = height / 2

    x_speed = 0
    y_speed = 0

    snake_pixels = []
    snake_length = 1

     #Создаем еду при помоши рандома

    target_x = round(random.randrange(0, width-snake_size) / 10.0) * 10.0
    target_y = round(random.randrange(0, height-snake_size) / 10.0) * 10.0

    #Cоздаем основной цикл где будет вся логика нашей игры

    while not game_over:

        #Создаем условия при котрых мы будем проигравыть и создаем надпись "Game Over"

        while game_close:
            game_display.fill(black)
            game_over_message = message_font.render("Game Over!", True, red)
            game_display.blit(game_over_message, [width / 3, height / 3])
            print_score(snake_length - 1)
            pygame.display.update()

            #При помощи этого цикла создаем условия при нажатии клавиши 1 мы выходим из игры, при нажатии на 2 начинаем заново

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_2:
                        run_game()
                    if event.type == pygame.QUIT:
                        game_over = True
                        game_close = False


         #Основной цикли, пишем условия при нажатии на клавиши вверх вниз влево вправо

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = -snake_size
                    y_speed = 0

                if event.key == pygame.K_RIGHT:
                    x_speed = snake_size
                    y_speed = 0

                if event.key == pygame.K_UP:
                    x_speed = 0
                    y_speed = -snake_size

                if event.key == pygame.K_DOWN:
                    x_speed = 0
                    y_speed = snake_size

                    #Логика проигрыша если х больше чем ширина карты и у больше чем длина карты это значит что змейка выходит за пределы и происходит удар 

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

            #Запускаем клавиши и при нажатии происходит движение змеки по карте

        x += x_speed
        y += y_speed

        #Ставим цвет дисплею черный, еде оранжевый, и змеке оранжевый

        game_display.fill(black)
        pygame.draw.rect(game_display, orange, [target_x, target_y, snake_size, snake_size])

        snake_pixels.append([x,y])

        if len(snake_pixels) > snake_length:
            del snake_pixels[0]

            #Прописываем циклы если змейка врезается сама в себе то мы проигрываем и высвечивается надпись Game over

        for pixel in snake_pixels[:-1]:
            if pixel == [x, y]:
                game_close = True

                #используем методы чтобы нарисовать змеку и наш счет на поле игры

        draw_snake(snake_size, snake_pixels)
        print_score(snake_length - 1)

        pygame.display.update()

        #Пишем логику при коорой если змека сьедает еду то она вырастает и еда появляется заново в рандомном месте

        if x == target_x and y == target_y:
            target_x = round(random.randrange(0, width-snake_size) / 10.0) * 10.0
            target_y = round(random.randrange(0, height-snake_size) / 10.0) * 10.0
            snake_length += 1

            #Запускаем таймер 

        clock.tick(snake_speed)

        #Прописываем выход из игры и вызов функции 


    pygame.quit()
    quit()

run_game()