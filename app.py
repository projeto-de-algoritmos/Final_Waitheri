import game as gm

import pyxel

class App:
    def __init__(self):
        pyxel.init(256, 256, caption="")
        
        pyxel.mouse(True)
        self.game = gm.Game()

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btnp(pyxel.KEY_R):
            self.game = gm.Game()
            for i in range(14):
                for j in range(13):
                    print(self.game.graph[j][i], end=' ')
                print()
            print()

    def draw(self):
        pyxel.cls(0)

        pyxel.load("assets.pyxres")
        for i in range(14):
            for j in range(13):
                # FIXME: Consertar esse demônio de renderização
                if self.game.graph[j][i] == 0: pyxel.blt(8 + 16*i, 8 + 16*j, 0, 16, 16, 32, 32)

App()
