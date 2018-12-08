import robot
r = robot.rmap()


def task1:
    r.lm('task1')
    r.up()
    r.rt()
    r.dn()
    r.rt()
    r.up()
    r.rt()
    r.dn()


def task2:
    r.lm('task2')
    for i in range(5):
        r.up()
        r.pt()
        r.rt()
        r.dn()
        r.pt()
        r.up(2)
        r.pt()
        r.rt()
        r.dn()
        r.pt()
        r.dn()
        r.rt()


def task3:
    r.lm('task3')
    r.rt()
    for i in range(8):
        if r.fd():
            r.dn()
            r.up()
        r.rt()


def task4:
    r.lm('task4')
    while not r.wu():
        r.up()
    while not r.wr():
        r.rt()
    r.lt()
    for i in range(5):
        for j in range(3):
            r.dn()
            r.pt()
            r.dn()
        r.up(5)
        r.lt()


def task5:
    r.lm('task5')
    for i in range(3):
        for j in range(5):
            r.pt()
            r.dn()
            r.rt()
            r.pt()
            r.up()
            r.rt()
            r.pt()
            if not r.wr():
                r.rt()
        if not r.wd():
            r.dn(3)
            r.lt(14)


def task6:
    r.lm('task6')
    width = int(input("Введите ширину: "))
    height = int(input("Введите высоту: "))

    if not width % 2:
        width += 1
    for i in range(width):
        r.pt()
        r.rt()
    r.lt(int(width/2) + 1)
    for i in range(height):
        r.pt()
        r.dn()

        
r.start(task1)
