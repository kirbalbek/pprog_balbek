import sys
import pygame

pygame.init()

width = 800
height = 500

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Ball')
clock = pygame.time.Clock()

x = 30
y = 30
vx = 50
vy = 50

while True:
    dt = clock.tick(50) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if x >= width-20 or x < 20:            #Отталкивание шарика
        vx = -vx
    if y >= height-20 or y < 20:
        vy = -vy

    if pygame.key.get_pressed()[pygame.K_UP]:
        vy-=5
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        vy+=5
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        vx-=5
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        vx+=5

    x += vx * dt
    y += vy * dt


    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (150, 10, 50), (int(x), int(y)), 20)

    pygame.display.flip()
