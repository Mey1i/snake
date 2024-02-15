import pygame
from random import randrange


#PARAMETRS SET START
RES = 800
SIZE = 50 

x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
dirs = {'W': True, 'S': True, 'A': True, 'D': True}
length = 1
snake = [(x, y)]
dx, dy = 0, 0
score = 0
fps = 5
#PARAMETRS SET END



pygame.init()
sc = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 26, bold=True)
font_end = pygame.font.SysFont('Arial', 66, bold=True)
img = pygame.image.load("images/background.jpg").convert()
img = pygame.transform.scale(img, (RES, RES))

# Загрузка изображения иконки
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("Snake")
game_over = False

while True:
    sc.fill(pygame.Color('Black'))
    sc.blit(img, (0, 0))
    [(pygame.draw.rect(sc, pygame.Color('green'), (i, j, SIZE-2, SIZE-2))) for i, j in snake]
    pygame.draw.rect(sc, pygame.Color('red'), (*apple, SIZE, SIZE))
    # render score
    render_score = font_score.render(f'SCORE:{score}', 1, pygame.Color('orange'))
    sc.blit(render_score, (5, 5))
    x += dx * SIZE
    y += dy * SIZE
    snake.append((x, y))
    snake = snake[-length:]

    if snake[-1] == apple:
        apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
        length += 1 
        score += 1
        fps += 1
    # game rules
    if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE or len(snake) != len(set(snake)):
        game_over = True
        while game_over:
            render_end = font_end.render('GAME OVER', 1, pygame.Color('orange'))
            sc.blit(render_end, (RES // 2 - 200, RES // 3))
            render_restart = font_score.render('Press "R" to restart', 1, pygame.Color('orange'))
            sc.blit(render_restart, (RES // 2 - 160, RES // 2))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        game_over = False
                        # Сброс игровых параметров
                        x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
                        apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
                        dirs = {'W': True, 'S': True, 'A': True, 'D': True}
                        length = 1
                        snake = [(x, y)]
                        dx, dy = 0, 0
                        score = 0
                        fps = 5
                        break

    pygame.display.flip()
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()




#MOVEMENT RULES START
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and dirs['W']:
        dx, dy = 0, -1
        dirs = {'W': True, 'S': False, 'A': True, 'D': True}
    if key[pygame.K_s] and dirs['S']:
        dx, dy = 0, 1
        dirs = {'W': False, 'S': True, 'A': True, 'D': True}
    if key[pygame.K_a] and dirs['A']:
        dx, dy = -1, 0
        dirs = {'W': True, 'S': True, 'A': True, 'D': False}
    if key[pygame.K_d] and dirs['D']:
        dx, dy = 1, 0
        dirs = {'W': True, 'S': True, 'A': False, 'D': True}
#MOVEMENT RULES END
