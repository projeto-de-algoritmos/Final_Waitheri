import utils as ut
import text as tx
import button as bt
import coin as cs
import game as gm

import pyxel
import random as rand


def update_menu(game):
    if game.botao_start.update() == 1:
        game.game_status = ut.PLAYING_STATUS

def draw_menu(game):
    draw_frame_boarding()
    game.botao_start.draw()
    pyxel.blt((ut.TAM_SCREEN/2) - 55, 53, 1, 64, 8, 175, 108)

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
        game.game_status = ut.STORE_STATUS
        game.opened_store = True and ut.ONE_STORE_PER_ROOM

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

    draw_frame_boarding()
    draw_player_status(game)

#TODO: Se der tempo adicionar o bot??o de resetar cartas
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
        discount = rand.choice(ut.DISCOUNTS)
        game.discount_game = cs.Coin_game(
            discount[1][0], discount[1][1], discount[1][2],
            discount[0]
        )

def draw_store(game, buttons):
    draw_frame_boarding()
    pyxel.blt(80, 25, 1, 104, 160, 95, 18)
    for i in range(len(game.store.itens)):
        item = game.store.itens[i]
        if buttons[i].valid:
            tx.Centered_text(
                item.item, 
                70, 
                10, 
                18 + i * 58,
            ).draw()
            pyxel.blt(18 + i * 58, 80, 0, 48, 64, 48, 64, 0)
            if item.item == 'Coracao':
                pyxel.blt(18 + i * 58 + 16, 80 + 24, 0, 64, 0, 16, 16, 0)
            else:
                pyxel.blt(18 + i * 58 + 16, 80 + 24, 0, 64, 16, 16, 16, 2)
            pyxel.blt(46 + i * 58, 134, 0, 80, 8, 8, 8, 0)
            pyxel.blt(50 + i * 58, 125, 0, 72 + item.amount * 16, 0, 16, 16, 0)
        else:
            pyxel.blt(18 + i * 58, 80, 0, 0, 64, 48, 64, 0)
        buttons[i].draw()

    for i in range(len(game.store.itens), len(game.store.itens) + 1):
        buttons[i].draw()

    draw_player_status(game)

def generate_discount_buttons(game):
    buttons = []
    buttons.append(bt.Normal_button(30 * 0 + 90, ut.TAM_SCREEN/2 + 40, str(1)))
    buttons.append(bt.Normal_button(30 * 1 + 90, ut.TAM_SCREEN/2+ 40, str(game.discount_game.retira1)))
    buttons.append(bt.Normal_button(30 * 2 + 90, ut.TAM_SCREEN/2+ 40, str(game.discount_game.retira2)))
    return buttons

def update_discount(game, buttons, store_buttons):
    discount_game = game.discount_game
    if discount_game.player == 1:
        if buttons[0].update() == 1 and discount_game.qtdMoedas - 1 >= 0:
            discount_game.qtdMoedas -= 1
            discount_game.player = 0
        elif buttons[1].update() == 1 and discount_game.qtdMoedas - discount_game.retira1 >= 0:
            discount_game.qtdMoedas -= discount_game.retira1
            discount_game.player = 0
        elif buttons[2].update() == 1 and discount_game.qtdMoedas - discount_game.retira2 >= 0:
            discount_game.qtdMoedas -= discount_game.retira2
            discount_game.player = 0
    elif discount_game.qtdMoedas > 0 and discount_game.player == 0:
        discount_game.qtdMoedas -= discount_game.calculate_move()
        discount_game.player = 1
        
    if discount_game.qtdMoedas == 0:
        game.game_status = ut.STORE_STATUS
        game.store.apply_discount(discount_game.discount, discount_game.player)
        for i in range(len(game.store.itens)):
            store_buttons[i].update_value(str(game.store.itens[i]))
        store_buttons[4].valid = False

def draw_discount(game, buttons):
    draw_frame_boarding()
    pyxel.blt(ut.TAM_SCREEN/4 + 10, 30, 1, 121, 193, 108, 22)
    
    
    for button in buttons: button.draw()
    tx.Centered_text(('Quantidade de moedas restantes '+ str(game.discount_game.qtdMoedas)), ut.TAM_SCREEN/4 + 10, 7, ut.TAM_SCREEN/4).draw()
    x_coin = (ut.TAM_SCREEN/2) - 40 + 3
    y_coin = (ut.TAM_SCREEN/2) - 20 + 4
    pyxel.blt(x_coin - 3, y_coin - 4, 1, 31, 200, 72, 48)
    i = 0
    for coin in range(1, game.discount_game.qtdMoedas + 1):
        pyxel.blt(x_coin + (i*8), y_coin, 1, 50, 188, 4, 3)
        if i == 6:
            i = 0
            y_coin += 4
        else:
            i += 1

def update_final(game, rooms_completed):
    ...

def draw_final(game, rooms_completed):
    pyxel.blt(0, 0, 2, 0, 0, 256, 256, 0)
    pyxel.blt((ut.TAM_SCREEN/2) - 56, 53, 1, 88, 136, 139, 15)

    string = 'Moedas coletadas'
    tx.Centered_text(string, 90, 10, ut.TAM_SCREEN//2 - (len(string) * pyxel.FONT_WIDTH)//2).draw()
    string = str(game.player.coins_colected)
    tx.Centered_text(string, 100, 10, ut.TAM_SCREEN//2 - (len(string) * pyxel.FONT_WIDTH)//2).draw()

    string = 'Salas completas'
    tx.Centered_text(string, 120, 3, ut.TAM_SCREEN//2 - (len(string) * pyxel.FONT_WIDTH)//2).draw()
    string = str(rooms_completed)
    tx.Centered_text(string, 130, 3, ut.TAM_SCREEN//2 - (len(string) * pyxel.FONT_WIDTH)//2).draw()
    
    game.botao_final.draw()

def draw_frame_boarding():
    pyxel.blt(0, 0, 2, 0, 0, 256, 256, 0)

def draw_player_status(game):
    for i in range(game.player.lifes):
        pyxel.blt(16 + i * 18, 224, 0, 64, 0, 16, 16, 0)

    pyxel.blt(78, 224, 0, 16, 0, 16, 16, 0)
    pyxel.blt(96, 233, 0, 80, 24, 8, 8, 0)
    moedas = str(game.player.coins)
    for i in range(len(moedas)):
        num = int(moedas[i])
        if num == 0: num = 10
        pyxel.blt(99 + i * 11, 224, 0, 88 + (num - 1) * 16, 16, 16, 16, 0)

    pyxel.blt(156, 224, 0, 64, 16, 16, 16, 2)
    pyxel.blt(174, 233, 0, 80, 40, 8, 8, 0)
    passos = str(game.player.remaining_steps)
    for i in range(len(passos)):
        num = int(passos[i])
        if num == 0: num = 10
        pyxel.blt(177 + i * 11, 224, 0, 88 + (num - 1) * 16, 32, 16, 16, 0)
