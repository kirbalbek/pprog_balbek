from tkinter import *
from random import randrange as rnd, choice

root = Tk()
root.geometry('800x600')
width = 800
height = 600
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)
colors = ['red', 'gray', 'black']
ball_number = rnd(5, 10)  #количество мячей
balls = []  #массив мячей
r = rnd(10, 30) #радиус мячей
canv.create_text(400, 100, text = 'ничего интересного. шарики летают.')

for j in range(ball_number):
    x = rnd(r, width - r)
    y = rnd(r, height - r)
    dx = rnd(1, 10)
    dy = rnd(1, 10)
    circle = canv.create_oval(x - r, y - r, x + r, y + r, fill=choice(colors))
    ball = [x, y, dx, dy, circle]
    balls.append(ball)


def lever(): #функция, описывающая "рукоятку" скорости
    global balls
    for i in range(len(balls)):
        x_i, y_i, dx_i, dy_i, circle_i = balls[i]
        x_i += dx_i
        y_i += dy_i
        if x_i < 0:
            dx_i = -dx_i
            x_i = 0
        elif x_i > width - r:
            dx_i = -dx_i
            x_i = width - r
        if y_i < 0:
            dy_i = -dy_i
            y_i = 0
        elif y_i > height - r:
            dy_i = -dy_i
            y_i = height - r
        balls[i] = [x_i, y_i, dx_i, dy_i, circle_i]
        canv.move(circle_i, dx_i, dy_i)


def timer(): #фунцкия, описывающая протяженность интервала между
		# движениями шариков
    global freeze
    speed = speed_scale.get()
    if speed == 0:
        freeze = True
        return
    lever()
    sleep = 110 - 10 * speed
    root.after(sleep, timer)


def unfreezer(event):
    global freeze
    if freeze:
        speed = speed_scale.get()
        if speed != 0:
            freeze = False
            root.after(0, timer)


speed_scale = Scale(root, orient=HORIZONTAL, length=300,
		 from_=0, to=10, tickinterval=1, resolution=1)
#шкала
speed_scale.pack()
speed_scale.set(10)
freeze = False
root.after(10, timer)
speed_scale.bind("<Motion>", unfreezer)

root.mainloop()
