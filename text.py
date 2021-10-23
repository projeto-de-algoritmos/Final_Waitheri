import pyxel
import utils as ut


class Centered_text:
    def __init__(self, text, y, col, x):
        self.text = text
        self.tam = len(self.text) * pyxel.FONT_WIDTH
        self.x = x
        self.y = y
        self.col = col

    def update(self, text):
        self.text = text

    def draw(self):
        pyxel.text(self.x, self.y, self.text, self.col)
