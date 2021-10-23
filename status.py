import utils as ut
import text as tx
import button as bt

import pyxel
import game as gm


def update_menu(game):
    if game.botao_start.update() == 1:
        game.game_status = ut.PLAYING_STATUS

def draw_menu(game):
    game.botao_start.draw()
    pyxel.blt((ut.TAM_SCREEN/2) - 60, 53, 1, 64, 8, 175, 108)

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

    # Caso se prefira abrir a loja apenas uma vez por quarto
    #  if pyxel.btnp(pyxel.KEY_L) and not game.opened_store:
    #      game.opened_store = True
    #      game.game_status = ut.STORE_STATUS

    if pyxel.btnp(pyxel.KEY_L):
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

def generate_store_buttons(game):
    buttons = []
    for i in range(len(game.store.itens)):
        item = game.store.itens[i]
        buttons.append(bt.Normal_button(
            len(str(item)) + (20 if item.get_value() < 10 else 16) + i * 58,
            149, 
            str(item)
        ))
    buttons.append(bt.Normal_button(
        ut.TAM_SCREEN / 2 - len('Desconto') * pyxel.FONT_WIDTH + 20,
        171, 
        'Desconto'
    ))

    #TODO: Se der tempo adicionar o botão de restart das cartas
    #  buttons.append(bt.Normal_button(
    #      len(str(item)) + (20 if item.get_value() < 10 else 16) + i * 58,
    #      169, 
    #      str(item)
    #  ))
    return buttons

def update_store(game, buttons):
    if pyxel.btnp(pyxel.KEY_L):
        game.game_status = ut.PLAYING_STATUS

    for i in range(len(game.store.itens)):
        button = buttons[i]
        item = game.store.itens[i]
        if button.update() == 1:
            if game.store.validate_purchase(game.player.coins, item):
                button.valid = False
                game.player.coins -= item.get_value()
                if item.item == 'Coracao':
                    game.player.lifes += item.amount
                    if game.player.lifes > 3: game.player.lifes = 3
                elif item.item == 'Passo':
                    game.player.remaining_steps += item.amount

    if buttons[len(game.store.itens)].update() == 1:
        game.game_status = ut.DISCOUNT_STATUS

def draw_store(game, buttons):
    for i in range(len(game.store.itens)):
        item = game.store.itens[i]
        tx.Centered_text(
            item.item, 
            70, 
            10, 
            18 + i * 58,
        ).draw()
        pyxel.blt(18 + i * 58, 80, 0, 0, 64, 48, 64, 0)
        buttons[i].draw()

    for i in range(len(game.store.itens), len(game.store.itens) + 1):
        buttons[i].draw()

def update_discount():
    ...

def draw_discount():
    ...

def update_final(game, rooms_completed):
    ...

def draw_final(game):
    pyxel.blt((ut.TAM_SCREEN/2) - 60, 53, 1, 88, 136, 202, 151)
    #TODO: adicionar quantidade de moedas coletadas
    #TODO: adicionar quantidade de quartos percorridos
    game.botao_final.draw()
