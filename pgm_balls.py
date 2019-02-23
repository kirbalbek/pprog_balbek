import pygame
import random as rnd
                                        #глобальные переменные
BACKGROUND = (0, 0, 0)
RADIUS = 20
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
VELOCITY = 0
NUMBER_OF_BALLS = 10

def speed_count(v_onx, v_ony):          #функция для расчета скорости
    v_final = (v_onx ** 2 + v_ony ** 2) ** 0.5
    return v_final


class Ball:                             #класс для основных характеристик шаров
    def __init__(self):
        self.x = 0
        self.y = 0
        self.dx = 0
        self.dy = 0
        self.color = (100, 100, 100)
        self.radius = RADIUS


def create_ball():                      #функция для создания шара
    ball = Ball()
    ball.x = rnd.randrange(ball.radius, SCREEN_WIDTH - ball.radius)
    ball.y = rnd.randrange(ball.radius, SCREEN_HEIGHT - ball.radius)
    ball.dx = rnd.randrange(1, 7)
    ball.dy = rnd.randrange(1, 7)
    VELOCITY = speed_count(ball.dx, ball.dy)*30     #определение цвета...
    if VELOCITY > 255:                              #...от скорости
        VELOCITY = 255
    ball.color = (VELOCITY, 100, 100)
    return ball


def main():
    pygame.init()
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Balls")
    clock = pygame.time.Clock()
    ball_list = []
    game_process = True
    for i in range (NUMBER_OF_BALLS):
        ball = create_ball()
        ball_list.append(ball)
    while game_process:                             #бесконечный цикл
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_process = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    ball = make_ball()
                    ball_list.append(ball)
        for ball in ball_list:
            ball.x += ball.dx
            ball.y += ball.dy


            if ball.y > SCREEN_HEIGHT - ball.radius or ball.y < ball.radius:
                ball.dy = - ball.dy
            if ball.x > SCREEN_WIDTH - ball.radius or ball.x < ball.radius:
                ball.dx = - ball.dx

        screen.fill(BACKGROUND)

        for ball in ball_list:
            pygame.draw.circle(screen, ball.color,
                            [ball.x, ball.y], ball.radius)
        clock.tick(60)
        pygame.display.flip()


if __name__ == "__main__":
     main()
