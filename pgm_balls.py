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
r = 20
x_second = 300
y_second = 400
vx_second = 165
vy_second = 165

while True:
    dt = clock.tick(50) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if x >= width - r or x < r:                    #Отталкивание шарика
        vx = -vx
    if y >= height - r or y < r:
        vy = -vy

    if x_second >= width - r or x_second < r:      #Отталкивание 2 шарика
        vx_second = -vx_second
    if y_second >= height - r or y_second < r:
        vy_second = -vy_second

    if pygame.key.get_pressed()[pygame.K_UP]:      #Ускорение по кнопкам
        vy-=5
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        vy+=5
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        vx-=5
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        vx+=5

    vx = vx*0.97                                    #Сопротивление воздуха
    vy = vy*0.97

    rgb_red = (vx**2+vy**2)**0.5                    #Определение цвета
    if rgb_red > 255:
        rgb_red = 255

    balls_dist = (abs(x-x_second)**2+abs(y-y_second)**2)**0.5
    if balls_dist<2*r:
        lenx = abs(vx - vx_second)
        leny = abs(vy - y_second)
        vy1 = vy - 2*vy*leny/((vx**2+vy**2)**0.5)
        vx1 = vx - 2*vx*leny/((vx**2+vy**2)**0.5)
        vy_second = vy_second - vy*leny/((vx_second**2+vy_second**2)**0.5)
        vx_second = vx_second - vx*leny/((vx_second**2+vy_second**2)**0.5)

    x += vx * dt
    y += vy * dt

    x_second += vx_second * dt
    y_second += vy_second * dt

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (int(rgb_red), 100, 100), (int(x), int(y)), int(r))
    pygame.draw.circle(screen, (235, 100, 100), (int(x_second), int(y_second)), int(r))

    pygame.display.flip()
