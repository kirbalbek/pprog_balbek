from tkinter import *
root = Tk()
root.geometry('800x600')
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

x = y = 300
r = 130
color = 'green'

# ваш код здесь

canv.create_oval(x-r,y-r,x+r,y+r, fill='red')

# конец вашего кода

mainloop()
