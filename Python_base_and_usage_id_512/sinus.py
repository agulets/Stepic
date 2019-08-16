from tkinter import *
from random import choice
import math
colors = ["#ee1f34", "#ff6347", "#00ff00", "#ffd700", "#d18dc9", "#940722"]

root = Tk()
root.title("Построение функции y=sin(X)")
root.geometry("1320x680")

canvas = Canvas(root, height=640, width=1040, bg="#fff")
canvas.pack(side="right")

for y in range(21):  # vertical
    k = 50 * y
    canvas.create_line(20 + k, 620, 20 + k, 20, width=1, fill="#ccc")

for x in range(13):  # horizontal
    k = 50 * x
    canvas.create_line(20, 20 + k, 1020, 20 + k, width=1, fill="#ccc")

# x,y lines
canvas.create_line(20, 20, 20, 620, width=1, arrow=FIRST, fill="#000")  # X
canvas.create_line(10, 320, 1020, 320, width=1, arrow=LAST, fill="#000")  # Y
canvas.create_text(20, 10, text="300", fill="#002")
canvas.create_text(20, 630, text="-300", fill="#002")
canvas.create_text(10, 310, text="0", fill="#002")
canvas.create_text(1030, 310, text="1000", fill="#002")

label_w = Label(root, text="Частота цикла:")
label_w.place(x=0, y=10)
label_phi = Label(root, text="Смещение по иксу:")
label_phi.place(x=0, y=30)
label_A = Label(root, text="Амплитуда:")
label_A.place(x=0, y=50)
label_dY = Label(root, text="Смещение по игрек:")
label_dY.place(x=0, y=70)

entry_w = Entry(root)
entry_w.place(x=150, y=10)
entry_phi = Entry(root)
entry_phi.place(x=150, y=30)
entry_A = Entry(root)
entry_A.place(x=150, y=50)
entry_dY = Entry(root)
entry_dY.place(x=150, y=70)


def sinus(w, phi, a, dy):
    global sin
    sin = 0
    xy = []
    for x in range(1000):
        y = math.sin(x * w)
        xy.append(x + phi)
        xy.append(y * a + dy)
    sin = canvas.create_line(xy, fill=choice(colors))


def clean():
    canvas.delete(sin)


btn_calc = Button(root, text="Рассчитать")
btn_calc.bind("<Button-1>", lambda event: sinus(float(entry_w.get()),
                                                float(entry_phi.get()),
                                                float(entry_A.get()),
                                                float(entry_dY.get())))
btn_calc.place(x=10, y=100)

btn_clean = Button(root, text="Очистить")
btn_clean.bind("<Button-1>", lambda event: clean())
btn_clean.place(x=100, y=100)

btn_default = Button(root, text="По умолчанию")
btn_default.bind("<Button-1>", lambda event: sinus(0.0209, 20, 200, 320))
btn_default.place(x=10, y=150)
root = mainloop()
