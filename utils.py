class Vect2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.x}, {self.y})'

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

# Dicionário de itens da loja no formato:
# dict = {"Nome": (probabilidade, [qtd, ...], (preçoMin, preçoMax))}
#TODO: se der tempo, adicionar habilidade
STORE_ITENS = {
    "Coracao": (
        30,
        [1, 2],
        (4, 7)
    ),
    "Passo": (
        100,
        [2, 3, 4],
        (2, 8)
    )
}

# dict = [(desconto, (qtdMoedas, qtd1, qtd2), descontoAum]
DISCOUNTS = [
        (20, (), 10),
        (30, (), 15),
        (40, (), 20),
        (50, (), 25)]
