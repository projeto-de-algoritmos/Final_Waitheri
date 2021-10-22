class Vect2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.x}, {self.y})'

# Screen
TAM_SCREEN = 256

# Possíveis estados do jogo
MENU_STATUS = 0
PLAYING_STATUS = 1
STORE_STATUS = 2
DISCOUNT_STATUS = 3
FINAL_STATUS = 4
NEW_ROOM_STATUS = 5

# Tamanho da matriz do jogo
COLUMNS = 15
ROWS = 13

# Opções de geração dos quartos
MAX_WIDTH_ROOM = 2
MAX_HEIGHT_ROOM = 2
MIN_WIDTH_ROOM = 2
MIN_HEIGHT_ROOM = 2

QTD_ROOMS = 8

# (porcentagem, valorNaMatriz)
PER_FLOOR = (100, 1)
PER_WALL = (49, 2)
PER_SPIKE = (7, 3)

# Porcentagem de cair moeda quando quebrar a caixa
PER_COIN = 30

# Quantidade de itens na loja (recomendado deixar 3)
AMOUNT_ITENS_STORE = 3

# dict = {"Nome": ([qtd], (preçoMin, preçoMax))}
#FIXME: talvez seja necessário adicionar uma identificação pra quando for desenhar na tela
STORE_ITENS = {
        "Coração": (
            [1, 2],
            (4, 7)
        ),
        "Passo": (
            [2, 3, 4],
            (2, 8)
        ),
        "Habilidade": (
            [1],
            (8, 10)
        )}

# dict = [(desconto, (qtdMoedas, qtd1, qtd2), descontoAum]
DISCOUNTS = [
        (20, (), 10),
        (30, (), 15),
        (40, (), 20),
        (50, (), 25)]
