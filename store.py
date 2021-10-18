import utils as ut

import random as rand


class Item:
    def __init__(self, item, amount, price):
        self.item = item
        self.amount = amount
        self.price = price

class Store:
    #TODO: a princípio o discount é uma tupla (desconto se vitória, aumento se perda)
    def __init__(self, discount):
        self.itens = self.__init_itens()
        self.discount = discount
        # already_player é para evitar que ele fique pedindo descontos
        self.already_played = False

    def __init_itens(self):
        itens = []
        for i in range(ut.AMOUNT_ITENS_STORE):
            itens.append(Item(
                item = rand.choice(list(ut.STORE_ITENS)),
                amount = rand.choice(list(ut.STORE_ITENS[item][0])),
                price = rand.randint(ut.STORE_ITENS[item][1][0],ut.STORE_ITENS[item][1][1])
            ))

        return itens

    #TODO: lembrar de subtrair o valor no app e aplicar o efeito do item
    def validate_purchase(self, money, item):
        if money - item.price >= 0:
            self.itens.pop(item)
            return True
        return False

    def apply_discount(self, winner):
        for item in self.itens:
            if winner == 1: item.price *= (100 - self.discount[0])
            else: item.price *= (100 - self.discount[0])

