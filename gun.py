from tkinter import *
from random import randrange as rnd, choice
import math
import time

root = Tk()
root.geometry('800x600')
width = 600
height = 800

canv = Canvas(root, bg='peach puff')
canv.pack(fill=BOTH, expand=1)
colors = ['red',  'gray', 'black']


class Ball: # Класс, задающий ""пули""
    def __init__(self):
        self.x = 50
        self.y = 50
        self.r = 10
        self.color = 'black'
        self.circle = canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r,
                                       fill=self.color)
        self.live = 1


    def coord(self):
        canv.coords(self.circle, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)


    def move(self): #функция, описывающая физику движения
        if self.y <= 500:
            self.dy -= 1.2
            self.y -= self.dy
            self.x += self.dx
            self.dx *= 0.99
            self.coord()
        else:
            if self.dx**2+self.dy**2 > 10:
                self.dy = -self.dy/2
                self.dx = self.dx/2
                self.y = 499
            if self.live < 0:
                balls.pop(balls.index(self))
                canv.delete(self.circle)
            else:
                self.live -= 1
        if self.x > 780:
            self.dx = - self.dx/2
            self.x = 779

    def collision(self, ball):  #проверка, попала ли пуля в цель
        if abs(ball.x - self.x) <= (self.r + ball.r) and abs(ball.y - self.y) <= (self.r + ball.r):
            return True
        else:
            return False


class Gun: #описывается пушка
    def __init__(self):
        self.power = 10
        self.on = 0
        self.angle = 1
        self.cannon = canv.create_line(30, 50, 60, 20, width=7)

    def begin_shoot(self, event):
        self.on = 1

    def end_shoot(self, event):
        global balls, bullet
        bullet += 1
        new_ball = Ball()
        new_ball.r += 3
        self.angle = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        new_ball.dx = self.power * math.cos(self.angle)
        new_ball.dy = -self.power * math.sin(self.angle)
        balls.append(new_ball)
        self.on = 0
        self.power = 10

    def targetting(self, event=0):
        if event:
            self.angle = math.atan((event.y - 50) / (event.x - 20))
        canv.coords(self.cannon, 20, 50, 20 + max(self.power, 20) * math.cos(self.angle),
                    50 + max(self.power, 20) * math.sin(self.angle))

    def power_up(self):
        if self.on:
            if self.power < 200:
                self.power += 2


class target():
    def __init__(self):
        self.points = 0
        self.circle = canv.create_oval(0, 0, 0, 0)
        self.point = canv.create_text(750, 50, text=self.points, font='28')
        self.new_target()
        self.live = 1

    def new_target(self):
        x = self.x = rnd(400, 780)
        y = self.y = rnd(100, 400)
        r = self.r = rnd(10, 50)
        color = self.color = 'red'
        canv.coords(self.circle, x - r, y - r, x + r, y + r)
        canv.itemconfig(self.circle, fill=color)

    def hit(self, points=1):
        canv.coords(self.circle, -10, -10, -10, -10)
        self.points += points
        canv.itemconfig(self.point, text=self.points)


tg = target()
screen = canv.create_text(700, 30, text='Удачи!', font='28')
gn = Gun()
bullet = 0
balls = []


def new_game(event=''):
    global Gun, tg, screen, balls, bullet
    tg.new_target()
    bullet = 0
    balls = []
    canv.bind('<Button-1>', gn.begin_shoot)
    canv.bind('<ButtonRelease-1>', gn.end_shoot)
    canv.bind('<Motion>', gn.targetting)

    tg.live = 1
    while balls or tg.live:
        for ball_y in balls:
            ball_y.move()
            if ball_y.collision(tg) and tg.live:
                tg.live = 0
                tg.hit()
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
        canv.update()
        time.sleep(0.03)
        gn.targetting()
        gn.power_up()
    canv.itemconfig(screen, text='')
    canv.delete(Gun)
    root.after(200, new_game)


new_game()

mainloop()
