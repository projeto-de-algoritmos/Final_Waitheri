import game as gm
import utils as ut

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
                    print(self.game.graph[i][j][0], end=' ')
                print()
            print()

        # TODO: adicionar movimentos player Tauz
        #  if pyxel.btnp(pyxel.KEY_UP):
        #      self.game.player.pos.x -= 1
        #  if pyxel.btnp(pyxel.KEY_DOWN):
        #      self.game.player.pos.x += 1
        #  if pyxel.btnp(pyxel.KEY_LEFT):
        #      self.game.player.pos.y -= 1
        #  if pyxel.btnp(pyxel.KEY_RIGHT):
        #      self.game.player.pos.y += 1

    def draw(self):
        pyxel.cls(0)

        pyxel.load("assets.pyxres")
        for i in range(self.game.size.x):
            for j in range(self.game.size.y):
                if self.game.graph[j][i][0] == 0: pyxel.blt(8 + 16*i, 8 + 16*j, 0, 16, 16, 16, 16)
                else: pyxel.blt(8 + 16*i, 8 + 16*j, 0, 0, 16, 16, 16)

                if self.game.graph[j][i][0] == ut.PER_WALL[1]: pyxel.blt(8 + 16*i, 8 + 16*j, 0, 32, 0, 16, 16, 0)
                elif self.game.graph[j][i][0] == ut.PER_SPIKE[1]: pyxel.blt(8 + 16*i, 8 + 16*j, 0, 48, 0, 16, 16, 7)

                if j == self.game.player.pos.y and i == self.game.player.pos.x: pyxel.blt(8 + 16*i, 8 + 16*j, 0, 0, 0, 16, 16, 0)
                elif j == self.game.key.y and i == self.game.key.x: pyxel.blt(8 + 16*i, 8 + 16*j, 0, 48, 16, 16, 16, 7)
                elif j == self.game.exit.y and i == self.game.exit.x: pyxel.blt(8 + 16*i, 8 + 16*j, 0, 16, 32, 16, 16, 0)
                
App()
