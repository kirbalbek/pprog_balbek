import graphics as gr

window = gr.GraphWin("Otkritiye Arena", 600, 600)
lawn = gr.Polygon(gr.Point(0, 400), gr.Point(0, 600),
                  gr.Point(600, 600), gr.Point(600, 400))  # лужайка
lawn.setFill('green')
sky = gr.Polygon(gr.Point(0, 0), gr.Point(0, 400),
                 gr.Point(600, 400), gr.Point(600, 0))  # небо
sky.setFill('blue')


def draw_spartak(x):  # Рисует лого Спартака и табличку под ним
    romb = gr.Polygon(gr.Point(x - 75, 150), gr.Point(x, 100),
                      gr.Point(x + 75, 150), gr.Point(x, 200))
    romb.setFill('red')
    romb.draw(window)
    stripe = gr.Polygon(gr.Point(x - 55, 164), gr.Point(x + 20, 113),
                        gr.Point(x + 55, 137), gr.Point(x - 20, 188))
    stripe.setFill('white')
    stripe.draw(window)
    letterc = gr.Text(gr.Point(x, 150), "с")
    letterc.setSize(35)
    letterc.setFill('red')
    letterc.draw(window)
    plate = gr.Polygon(gr.Point(x - 70, 200), gr.Point(x - 70, 250),
                       gr.Point(x + 70, 250), gr.Point(x + 70, 200))
    plate.setFill('white')
    plate.draw(window)
    post = gr.Polygon(gr.Point(x - 5, 250), gr.Point(x - 5, 500),
                      gr.Point(x + 5, 500), gr.Point(x + 5, 250))
    post.setFill('white')
    post.draw(window)
    lettername = gr.Text(gr.Point(x, 230), "Спартак Москва")
    lettername.setSize(10)
    lettername.setFill('red')
    lettername.draw(window)


def gate_bar(x):  # Рисует штанги
    bar = gr.Line(gr.Point(x, 400), gr.Point(x, 300))
    bar.setWidth(10)
    bar.setOutline('gray')
    bar.draw(window)


def net_right(x):  # Рисует сетку ворот справа
    netr = gr.Line(gr.Point(x, 300), gr.Point(x + 100, 400))
    netr.setWidth(3)
    netr.setOutline('white')
    netr.draw(window)


def net_left(x):  # Рисует сетку ворот слева
    netr = gr.Line(gr.Point(x, 400), gr.Point(x + 100, 300))
    netr.setWidth(3)
    netr.setOutline('white')
    netr.draw(window)


def liner_right(x):  # Рисует разметку справа
    lin = gr.Line(gr.Point(x, 400), gr.Point(x + 70, 600))
    lin.setWidth(15)
    lin.setOutline('white')
    lin.draw(window)


def liner_left(x):  # Рисует разметку слева
    lin = gr.Line(gr.Point(x, 400), gr.Point(x - 70, 600))
    lin.setWidth(15)
    lin.setOutline('white')
    lin.draw(window)


gatebar_up = gr.Line(gr.Point(195, 300), gr.Point(405, 300))
gatebar_up.setWidth(10)
gatebar_up.setOutline('gray')  # рисует перекладину ворот, в функцию вставлять не имеет смысла

linerup = gr.Line(gr.Point(145, 400), gr.Point(455, 400))
linerup.setWidth(5)
linerup.setOutline('white')

ball = gr.Circle(gr.Point(350, 500), 20)  # рисует мяч
ball.setFill('orange')

lawn.draw(window)
sky.draw(window)
draw_spartak(525)
draw_spartak(75)
liner_right(450)
liner_left(150)
linerup.draw(window)
for i in range(200, 301, 25):  # используется цикл, чтобы создать параллельные линии net_right и net_left
    net_right(i)
    net_left(i)
for i in range(200, 401, 200):  # используется цикл, чтобы нарисовать параллельные штанги
    gate_bar(i)

gatebar_up.draw(window)
ball.draw(window)
window.getMouse()
window.close()
