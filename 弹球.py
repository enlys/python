from tkinter import *
from tkinter import messagebox

import random
import time


class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        startx = [-3, -2, -1, 1, 2, 3]
        random.shuffle(startx)
        self.x = startx[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)   # top-left bottom-right  将画布函数coords赋值给创建的pos变量；画布函数coords：通过ID来返回画布上任何画出图画的当前x和y坐标，让小球通过屏幕壁进行来回反弹；coords函数返回四个数字组成的列表表示坐标（x1,y1,x2,y2），即：图形左上角和右下角的x,y坐标
        if pos[1] <= 0 or self.hit_paddle(pos) == True:
            self.y = -self.y
        if pos[0] <= 0 or pos[2] >= self.canvas_width:
            self.x = -self.x
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True

    def hit_paddle(self, pos):
        global score
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:#判断球碰到球拍没
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                score += 1
                return True
        return False

class Paddle:
    def __init__(self, canvas, color,width):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, width, 10, fill=color)
        self.x = 0
        self.y = 0
        self.canvas.move(self.id, 200, 300)
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all("<Key-Left>", self.turn_left)
        self.canvas.bind_all("<Key-Right>", self.turn_right)

    def draw(self):
        pos = self.canvas.coords(self.id)
        if pos[0] + self.x >= 0 and pos[2] + self.x <= self.canvas_width:
            self.canvas.move(self.id, self.x, 0)
        # self.x = 0

    def turn_left(self, event):
        self.x = -4

    def turn_right(self, event):
        self.x = 4

width = 0


def test1():
    global width2
    width2 = 200


def test2():
    global width2
    width2 = 100

width2 = 100
score = 0
tk = Tk()
tk.title("Game")
tk.resizable(0, 0)  # not resizable 桌面不可拉动
tk.wm_attributes("-topmost", 1)  # at top
btn1 = Button(tk, text='简单', command=test1)
btn2 = Button(tk, text='难', command=test2)


btn1.pack(side='left')
btn2.pack(side='left')
canvas = Canvas(tk, width=500, height=350, bd=0, highlightthickness=0,bg='skyblue')
canvas.pack()
canvas.create_line(1, 0, 1, 600, fill='red')
tk.update()
paddle = Paddle(canvas, 'blue', width2)
ball = Ball(canvas, paddle, 'red')
while True:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
    else:
        messagebox.showinfo(title='失败！', message="你的分数为：" + str(score))#弹窗
        break
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
