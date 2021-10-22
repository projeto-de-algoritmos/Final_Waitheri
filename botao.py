import pyxel
import random
import math

class Vect2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Normal_button:
    def __init__(self, x, y, text):
        self.pos = Vect2(x, y)
        self.size = len(text) * pyxel.FONT_WIDTH - 6
        self.text = text

    def update(self):
        mouse_pos = [pyxel.mouse_x, pyxel.mouse_y]
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and self.__check_button_hitbox(mouse_pos):
            return 1
    def update_value(self, text):
        self.text = text

    def draw(self):
        pyxel.rect(self.pos.x, self.pos.y + 2, self.size, 15, 3)
        pyxel.circ(self.pos.x, self.pos.y + 2 + 7, 7, 3)
        pyxel.circ(self.pos.x + self.size, self.pos.y + 2 + 7, 7, 3)
        pyxel.rect(self.pos.x, self.pos.y, self.size, 15, 11)
        pyxel.circ(self.pos.x, self.pos.y + 7, 7, 11)
        pyxel.circ(self.pos.x + self.size, self.pos.y + 7, 7, 11)
        pyxel.text(self.pos.x - 2, self.pos.y + pyxel.FONT_HEIGHT - 1, self.text, 7)

    def __check_button_hitbox(self, mouse_pos):
        if math.dist([self.pos.x, self.pos.y + 7], mouse_pos) < 7: return True
        elif mouse_pos[0] >= self.pos.x and mouse_pos[0] <= self.pos.x + self.size and mouse_pos[1] >= self.pos.y and mouse_pos[1] <= self.pos.y + 15: return True
        elif math.dist([self.pos.x + self.size, self.pos.y + 7], mouse_pos) < 7: return True
        return False

class Retangular_button:
    def __init__(self, x, y, text):
        self.pos = Vect2(x, y)
        self.size = len(text) * pyxel.FONT_WIDTH + 3
        self.text = text

    def update(self):
        mouse_pos = [pyxel.mouse_x, pyxel.mouse_y]
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and self.__check_button_hitbox(mouse_pos):
            return 1

    def draw(self):
        pyxel.rect(self.pos.x, self.pos.y + 2, self.size, 7, 3)
        pyxel.rect(self.pos.x, self.pos.y, self.size, 7, 11)
        pyxel.text(self.pos.x + 2, self.pos.y + 1, self.text, 7)

    def __check_button_hitbox(self, mouse_pos):
        if mouse_pos[0] >= self.pos.x and mouse_pos[0] <= self.pos.x + 6 and mouse_pos[1] >= self.pos.y and mouse_pos[1] <= self.pos.y + 7: return True
        return False
