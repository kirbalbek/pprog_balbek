import graphics as gr

window = gr.GraphWin("Otkritiye Arena", 600, 600)

lawn = gr.Polygon(gr.Point(0,400), gr.Point(0,600), gr.Point(600,600), gr.Point(600,400))
lawn.setFill('green')

sky = gr.Polygon(gr.Point(0,0), gr.Point(0,400), gr.Point(600,400), gr.Point(600,0))
sky.setFill('blue')
def draw_star():
    gr.Polygon(gr.Point())
def draw_spartak(x):
    romb = gr.Polygon(gr.Point(x-75,150), gr.Point(x,100), gr.Point(x+75,150), gr.Point(x,200))
    romb.setFill('red')
    romb.draw(window)
    stripe = gr.Polygon(gr.Point(x-55,164), gr.Point(x+20,113), gr.Point(x+55,137), gr.Point(x-20,188))
    stripe.setFill('white')
    stripe.draw(window)
    letterc = gr.Text(gr.Point(x, 150),"с")
    letterc.setSize(35)
    letterc.setFill('red')
    letterc.draw(window)
    plate = gr.Polygon(gr.Point(x-70,200), gr.Point(x-70,250), gr.Point(x+70,250), gr.Point(x+70,200))
    plate.setFill('white')
    plate.draw(window)
    post = gr.Polygon(gr.Point(x-5,250), gr.Point(x-5,500), gr.Point(x+5,500), gr.Point(x+5,250))
    post.setFill('white')
    post.draw(window)
    lettername = gr.Text(gr.Point(x, 230),"Спартак Москва")
    lettername.setSize(15)
    lettername.setFill('red')
    lettername.draw(window)
def gate_bar(x):
    bar = gr.Line(gr.Point(x, 400), gr.Point(x, 300))
    bar.setWidth(10)
    bar.setOutline('gray')
    bar.draw(window)

def net_right(x):
    netr = gr.Line(gr.Point(x, 300), gr.Point(x+100, 400))
    netr.setWidth(3)
    netr.setOutline('white')
    netr.draw(window)
def net_left(x):
    netr = gr.Line(gr.Point(x, 400), gr.Point(x+100, 300))
    netr.setWidth(3)
    netr.setOutline('white')
    netr.draw(window)

lineright = gr.Line(gr.Point(450, 400), gr.Point(520, 600))
lineright.setWidth(15)
lineright.setOutline('white')

linerleft = gr.Line(gr.Point(150, 400), gr.Point(80, 600))
linerleft.setWidth(15)
linerleft.setOutline('white')


gatebar_up = gr.Line(gr.Point(195, 300), gr.Point(405, 300))
gatebar_up.setWidth(10)
gatebar_up.setOutline('gray')

linerup = gr.Line(gr.Point(145, 400), gr.Point(455, 400))
linerup.setWidth(5)
linerup.setOutline('white')

ball = gr.Circle(gr.Point(350, 500), 20)
ball.setFill('orange')

lawn.draw(window)
sky.draw(window)
draw_spartak(525)
draw_spartak(75)
lineright.draw(window)
linerleft.draw(window)
linerup.draw(window)
net_right(200)
net_right(225)
net_right(250)
net_right(275)
net_right(300)
net_left(200)
net_left(225)
net_left(250)
net_left(275)
net_left(300)
gate_bar(200)
gate_bar(400)
gatebar_up.draw(window)
ball.draw(window)


window.getMouse()

window.close()
