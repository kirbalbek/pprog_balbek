import turtle
import test


def task2():
	"""
	Сохраните и выполните предыдущую программу. 
	"""
	turtle.shape('turtle')
	turtle.forward(50)
	turtle.left(90)
	turtle.forward(50)
	turtle.left(90)
	turtle.forward(50)
	turtle.right(90)
	turtle.forward(50)
	turtle.right(90)
	turtle.forward(50)
	
	
def draw_square(l):
	"""
	Нарисуйте квадрат.
	"""
	turtle.shape('turtle')
	for i in range (4):
		turtle.forward(l)
		turtle.left(90)
	
def draw_circle(l):
	"""
	Нарисуйте окружность.
	"""
	turtle.shape('turtle')
	for i in range (360):
		turtle.forward(l)
		turtle.left(1)
		
		
def multiple_squares(n):
	"""
	Нарисуйте 10 вложенных квадратов.
	"""
	turtle.shape('turtle')
	a = int(10)
	for i in range(n):
		draw_square(a)	
		turtle.penup()
		for j in range(2):
			turtle.right(90)
			turtle.forward(10)
		turtle.right(180)
		turtle.pendown()
		a+=20

def spider(n):
        '''
        Нарисуйте паука с n лапами. Пример n = 12:
        '''
        turtle.shape('turtle')
        for i in range (n):
                turtle.forward(50)
                turtle.stamp()
                turtle.right(180)
                turtle.forward(50)
                turtle.right(180)
                turtle.right(360/n)
def spiral(n):
        a = int(1)
        for i in range(360):
                turtle.forward(a)
                turtle.right(20)
                a+=0.1
def sqspiral(n):
        a=int(10)
        for i in range(n):
                for j in range (2):
                        turtle.forward(a)
                        turtle.left(90)
                a+=10
sqspiral(10)
