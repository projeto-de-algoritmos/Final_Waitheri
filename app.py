import game as gm
import utils as ut
import status as st

import pyxel

class App:
    def __init__(self):
        pyxel.init(ut.TAM_SCREEN, ut.TAM_SCREEN, caption="")
        
        pyxel.mouse(True)
        pyxel.load("assets.pyxres")

        #FIXME: Trocar para MENU_STATUS or PLAYING_STATUS
        self.game = gm.Game(ut.MENU_STATUS)
        self.rooms_completed = 0

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if self.game.game_status == ut.MENU_STATUS:
            st.update_menu(self.game)
        elif self.game.game_status == ut.PLAYING_STATUS:
            st.update_playing(self.game)
        elif self.game.game_status == ut.STORE_STATUS:
            st.update_store(self.game)
        elif self.game.game_status == ut.DISCOUNT_STATUS:
            st.update_discount()
        elif self.game.game_status == ut.FINAL_STATUS:
            st.update_final(self.game, self.rooms_completed)

        if self.game.game_status == ut.NEW_ROOM_STATUS:
            self.rooms_completed += 1
            self.game = gm.Game(ut.PLAYING_STATUS)

        if pyxel.btnp(pyxel.KEY_R) or ((self.game.botao_final.update() == 1) and self.game.game_status == ut.FINAL_STATUS):
            self.rooms_completed = 0
            self.game = gm.Game(ut.MENU_STATUS)

    def draw(self):
        pyxel.cls(0)

        if self.game.game_status == ut.MENU_STATUS:
            st.draw_menu(self.game)
        elif self.game.game_status == ut.PLAYING_STATUS:
            st.draw_playing(self.game, self.rooms_completed)
        elif self.game.game_status == ut.STORE_STATUS:
            st.draw_store()
        elif self.game.game_status == ut.DISCOUNT_STATUS:
            st.draw_discount()
        elif self.game.game_status == ut.FINAL_STATUS:
            st.draw_final(self.game)

App()
