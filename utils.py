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

# Opção de quantidade de quartos na geração
QTD_ROOMS = 8

# (porcentagem, valorNaMatriz)
PER_FLOOR = (100, 1)
PER_WALL = (49, 2)
PER_SPIKE = (7, 3)

# Porcentagem de cair moeda quando quebrar a caixa
PER_COIN = 30

# Quantidade de itens na loja (recomendado deixar no máximo 4)
AMOUNT_ITENS_STORE = 4

# Abrir a loja apenas uma vez por sala
ONE_STORE_PER_ROOM = False

# Dicionário de itens da loja no formato:
# dict = {"Nome": (probabilidade, [qtd, ...], (preçoMin, preçoMax))}
#TODO: se der tempo, adicionar habilidade
STORE_ITENS = {
    "Coracao": (
        30,
        [1, 2],
        (5, 7)
    ),
    "Passo": (
        100,
        [2, 3, 4],
        (3, 7)
    )
}

# Possíveis descontos na loja no formato
# vec = [((desconto, descontoDeAumento), (qtdMoedas, qtd1, qtd2))]
DISCOUNTS = [
    ((2, 1), (14, 2, 5)),
    ((3, 2), (10, 3, 4)),
    ((4, 3), (15, 3, 6)),
    ((5, 4), (17, 4, 5))
]
