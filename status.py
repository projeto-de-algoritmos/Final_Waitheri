import utils as ut
import game as gm
import text as tx

import pyxel


def update_menu():
    ...

def draw_menu():
    ...

def update_playing(game):
    if pyxel.btnp(pyxel.KEY_UP):
        game.player.move_up(game.graph)
    if pyxel.btnp(pyxel.KEY_DOWN):
        game.player.move_down(game.graph)
    if pyxel.btnp(pyxel.KEY_LEFT):
        game.player.move_left(game.graph)
    if pyxel.btnp(pyxel.KEY_RIGHT):
        game.player.move_right(game.graph)

    if game.player.pos.x == game.key.x and game.player.pos.y == game.key.y and not game.player.has_key:
        game.player.has_key = True

    if game.player.pos.x == game.exit.x and game.player.pos.y == game.exit.y and game.player.has_key:
        game.game_status = ut.NEW_ROOM_STATUS

    if game.player.lifes <= 0:
        game.game_status = ut.FINAL_STATUS

    if pyxel.btnp(pyxel.KEY_L) and not game.opened_store:
        game.opened_store = True
        game.game_status = ut.STORE_STATUS

def draw_playing(game, rooms_completed):
    for i in range(game.size.x):
        for j in range(game.size.y):
            if game.graph[j][i][0] == 0:
                pyxel.blt(8 + 16*i, 8 + 16*j, 0, 16, 16, 16, 16)
            else:
                pyxel.blt(8 + 16*i, 8 + 16*j, 0, 0, 16, 16, 16)

            if game.graph[j][i][0] == ut.PER_WALL[1]:
                pyxel.blt(8 + 16*i, 8 + 16*j, 0, 32, 0, 16, 16, 0)
            elif game.graph[j][i][0] == ut.PER_SPIKE[1]:
                pyxel.blt(8 + 16*i, 8 + 16*j, 0, 48, 0, 16, 16, 7)
            elif game.graph[j][i][0] == 4:
                pyxel.blt(8 + 16*i, 8 + 16*j, 0, 16, 0, 16, 16, 0)

            if j == game.player.pos.y and i == game.player.pos.x:
                pyxel.blt(8 + 16*i, 8 + 16*j, 0, 16, 32, 16, 16, 0)
            elif j == game.key.y and i == game.key.x and not game.player.has_key:
                pyxel.blt(8 + 16*i, 8 + 16*j, 0, 48, 16, 16, 16, 7)
            elif j == game.exit.y and i == game.exit.x: 
                pyxel.blt(8 + 16*i, 8 + 16*j, 0, 0, 48, 16, 16, 0)

    tx.Centered_text(str(game.player.lifes), 220, 7, 10).draw()
    tx.Centered_text(str(game.player.remaining_steps), 230, 7, 10).draw()
    tx.Centered_text(str(game.player.coins), 240, 7, 10).draw()
    tx.Centered_text(str(rooms_completed), 250, 7, 10).draw()

def update_store(game):
    if pyxel.btnp(pyxel.KEY_L):
        game.game_status = ut.PLAYING_STATUS

def draw_store():
    ...

def update_discount():
    ...

def draw_discount():
    ...

def update_final():
    ...

def draw_final():
    ...
