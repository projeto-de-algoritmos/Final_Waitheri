import pyxel

class App:
    def __init__(self):
        pyxel.init(256, 256, caption="")
        
        pyxel.mouse(True)

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)

        pyxel.load("assets.pyxres")
        for i in range(15):
            for j in range(13):
                pyxel.blt(8+ 16*i, 8+ 16*j, 0, 0, 0, 16, 16)

App()
