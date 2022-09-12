import math
from tkinter import *

window = Tk()
window.title('Fractal Tree')
canvas_size = 1200

canvas = Canvas(window, width=canvas_size, height=canvas_size)
canvas.pack()


class Branch:
    to_draw = []
    length_ratio = 0.7
    min_length = 1

    def __init__(self, x, y, length, angle):
        self.x = x
        self.y = y
        self.length = length
        self.angle = angle

        self.end_x = x + length * math.cos(angle)
        self.end_y = y + length * math.sin(angle)

    @classmethod
    def draw_all(cls):
        to_draw = cls.to_draw
        cls.to_draw = []
        for branch in to_draw:
            branch.draw()

        for branch in to_draw:
            branch.grow()

        if cls.to_draw:
            cls.draw_all()

    def grow(self):
        if self.length <= self.min_length:
            return
        self.to_draw.append(Branch(self.end_x, self.end_y, self.length * self.length_ratio, self.angle + math.pi / 6))
        self.to_draw.append(Branch(self.end_x, self.end_y, self.length * self.length_ratio, self.angle - math.pi / 6))

    def draw(self):
        canvas.create_line(self.x, self.y, self.end_x, self.end_y)
        window.update()


Branch.to_draw.append(Branch(canvas_size/2, canvas_size, 300, -math.pi / 2))

Branch.draw_all()

window.mainloop()
