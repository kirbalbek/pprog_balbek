from tkinter import *
import random
import time

root = Tk()
root.geometry('600x600')
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)


def new_ball():
    global X, Y, R, CIRCLE
    canv.delete(CIRCLE)
    randcol = lambda: random.randint(0,255)
    color = '#%02X%02X%02X' % (randcol(),randcol(),randcol())  #рандомный цвет в hex
    X = random.randint(100,500)
    Y = random.randint(100,500)
    R = random.randint(20,40)
    CIRCLE = canv.create_oval(X-R,Y-R,
                              X+R,Y+R,
                              fill=color,
                              width=0)  #создаем новый круг
    root.after(1000, new_ball)


def ball_caught(event):                 #функция проверки попадания по мячу
    global POINTS, STRING_OUTPUT
    if (event.x-X)**2+(event.y-Y)**2<=R**2: #определяем, попал ли курсор по кругу
        POINTS+=1                           #увеличиваем число очков на 1
    canv.delete(STRING_OUTPUT)          #удаляем строку со старым рез-татом
    canv.delete(CIRCLE)                 #удаляем круг, чтобы нельзя было "набить" очки
    STRING_OUTPUT = canv.create_text(300,50,
                                         text='Вы попали %s раз' % POINTS,
                                         font='Helvetica 20')
POINTS = 0
CIRCLE = canv.create_oval(-1,0,0,0)         #Создаем круг за пределами холста
STRING_OUTPUT = canv.create_text(300,50,
                                 text='Вы попали %s раз' % POINTS,
                                 font='Helvetiica 20')
canv.bind('<Button-1>', ball_caught)
new_ball()

mainloop()
