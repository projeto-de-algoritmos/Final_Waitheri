import game as gm
import utils as ut
import text as tx
import status as st

import pyxel

class App:
    def __init__(self):
        pyxel.init(256, 256, caption="")
        
        pyxel.mouse(True)
        self.game_status = ut.MENU_STATUS
        self.game = gm.Game()

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if self.game_status = ut.MENU_STATUS:
            st.update_menu()
        if self.game_status = ut.PLAYING_STATUS:
            st.update_playing()
        if self.game_status = ut.STORE_STATUS:
            st.update_store()
        if self.game_status = ut.DISCOUNT_STATUS:
            st.update_discount()
        if self.game_status = ut.FINAL_STATUS:
            st.update_final()

        if pyxel.btnp(pyxel.KEY_R):
            self.game = gm.Game()

        #TODO: mover esses ifs para o update_playing
        if pyxel.btnp(pyxel.KEY_UP):
            self.game.player.move_up(self.game.graph)
        if pyxel.btnp(pyxel.KEY_DOWN):
            self.game.player.move_down(self.game.graph)
        if pyxel.btnp(pyxel.KEY_LEFT):
            self.game.player.move_left(self.game.graph)
        if pyxel.btnp(pyxel.KEY_RIGHT):
            self.game.player.move_right(self.game.graph)

        #TODO: adicionar tela de final de jogo
        if self.game.player.lifes <= 0:
            self.game_status = ut.FINAL_STATUS
            #  self.game = gm.Game()

    def draw(self):
        pyxel.cls(0)

        if self.game_status = ut.MENU_STATUS:
            st.draw_menu()
        if self.game_status = ut.PLAYING_STATUS:
            st.draw_playing()
        if self.game_status = ut.STORE_STATUS:
            st.draw_store()
        if self.game_status = ut.DISCOUNT_STATUS:
            st.draw_discount()
        if self.game_status = ut.FINAL_STATUS:
            st.draw_final()

        #TODO: mover essa lógica para o draw_playing
        pyxel.load("assets.pyxres")
        for i in range(self.game.size.x):
            for j in range(self.game.size.y):
                if self.game.graph[j][i][0] == 0: pyxel.blt(8 + 16*i, 8 + 16*j, 0, 16, 16, 16, 16)
                else: pyxel.blt(8 + 16*i, 8 + 16*j, 0, 0, 16, 16, 16)

                if self.game.graph[j][i][0] == ut.PER_WALL[1]: pyxel.blt(8 + 16*i, 8 + 16*j, 0, 32, 0, 16, 16, 0)
                elif self.game.graph[j][i][0] == ut.PER_SPIKE[1]: pyxel.blt(8 + 16*i, 8 + 16*j, 0, 48, 0, 16, 16, 7)
                elif self.game.graph[j][i][0] == 4: pyxel.blt(8 + 16*i, 8 + 16*j, 0, 16, 0, 16, 16, 0)

                if j == self.game.player.pos.y and i == self.game.player.pos.x: pyxel.blt(8 + 16*i, 8 + 16*j, 0, 16, 32, 16, 16, 0)
                elif j == self.game.key.y and i == self.game.key.x: pyxel.blt(8 + 16*i, 8 + 16*j, 0, 48, 16, 16, 16, 7)
                elif j == self.game.exit.y and i == self.game.exit.x: pyxel.blt(8 + 16*i, 8 + 16*j, 0, 0, 48, 16, 16, 0)

        tx.Centered_text(str(self.game.player.lifes), 220, 7, 10).draw()
        tx.Centered_text(str(self.game.player.remaining_steps), 230, 7, 10).draw()
        tx.Centered_text(str(self.game.player.coins), 240, 7, 10).draw()
App()
