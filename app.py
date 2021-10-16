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
            for i in range(self.game.size.y):
                for j in range(self.game.size.x):
                    print(self.game.graph[i][j], end=' ')
                print()
            print()

    def draw(self):
        pyxel.cls(0)

        pyxel.load("assets.pyxres")
        for i in range(self.game.size.x):
            for j in range(self.game.size.y):
                if self.game.graph[j][i] == 0: pyxel.blt(8 + 16*i, 8 + 16*j, 0, 16, 16, 16, 16)
                else: pyxel.blt(8 + 16*i, 8 + 16*j, 0, 0, 16, 16, 16)

                if self.game.graph[j][i] == 2: pyxel.blt(8 + 16*i, 8 + 16*j, 0, 32, 0, 16, 16, 0)
                elif self.game.graph[j][i] == 3: pyxel.blt(8 + 16*i, 8 + 16*j, 0, 48, 0, 16, 16, 7)

App()
