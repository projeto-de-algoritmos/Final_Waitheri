import game as gm
import utils as ut
import status as st

import pyxel

class App:
    def __init__(self):
        pyxel.init(256, 256, caption="")
        
        pyxel.mouse(True)
        #FIXME: Trocar para MENU_STATUS
        self.game = gm.Game(ut.PLAYING_STATUS)

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if self.game.game_status == ut.MENU_STATUS:
            st.update_menu()
        if self.game.game_status == ut.PLAYING_STATUS:
            st.update_playing(self.game)
        if self.game.game_status == ut.STORE_STATUS:
            st.update_store()
        if self.game.game_status == ut.DISCOUNT_STATUS:
            st.update_discount()
        if self.game.game_status == ut.FINAL_STATUS:
            st.update_final()

        if pyxel.btnp(pyxel.KEY_R):
            self.game = gm.Game(ut.PLAYING_STATUS)

    def draw(self):
        pyxel.cls(0)

        if self.game.game_status == ut.MENU_STATUS:
            st.draw_menu()
        if self.game.game_status == ut.PLAYING_STATUS:
            st.draw_playing(self.game)
        if self.game.game_status == ut.STORE_STATUS:
            st.draw_store()
        if self.game.game_status == ut.DISCOUNT_STATUS:
            st.draw_discount()
        if self.game.game_status == ut.FINAL_STATUS:
            st.draw_final()

App()
