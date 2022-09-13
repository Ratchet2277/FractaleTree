import colorsys
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
    min_length = 2
    max_length = 300
    right_angle_delta = math.pi / 12
    left_angle_delta = math.pi / 12

    def __init__(self, x, y, length=None, angle=-math.pi / 2):
        self.x = x
        self.y = y
        if length is None or length > self.max_length:
            length = self.max_length
        self.length = length
        self.angle = angle

        self.end_x = x + length * math.cos(angle)
        self.end_y = y + length * math.sin(angle)

    def get_color(self):
        depth = round(math.log(self.length/self.max_length, self.length_ratio))
        hue = depth / round(math.log(self.min_length/self.max_length, self.length_ratio))
        (r, g, b) = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
        R, G, B = int(255 * r), int(255 * g), int(255 * b)
        return '#%02x%02x%02x' % (R, G, B)

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
        new_length = self.length * self.length_ratio
        if new_length <= self.min_length:
            return
        self.to_draw.append(Branch(self.end_x, self.end_y, new_length, self.angle + self.right_angle_delta))
        self.to_draw.append(Branch(self.end_x, self.end_y, new_length, self.angle - self.left_angle_delta))

    def draw(self):
        canvas.create_line(self.x, self.y, self.end_x, self.end_y, fill=self.get_color())
        window.update()


Branch.to_draw.append(Branch(canvas_size/2, canvas_size))

Branch.draw_all()

window.mainloop()
