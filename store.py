import utils as ut

import random as rand


class Item:
    def __init__(self, item, amount, price):
        self.item = item
        self.amount = amount
        self.price = price

    def __repr__(self):
        return str(self.get_value()) + ' moedas'

    def get_value(self):
        return self.amount * self.price

class Store:
    def __init__(self):
        self.itens = self.__init_itens()
        self.already_played = False

    def __init_itens(self):
        itens = []
        for i in range(ut.AMOUNT_ITENS_STORE):
            rand_item = rand.randint(1, 100)
            if rand_item <= ut.STORE_ITENS['Coracao'][0]:
                item = 'Coracao'
            else:
                item = 'Passo'
            amount = rand.choice(ut.STORE_ITENS[item][1])
            price = rand.randint(ut.STORE_ITENS[item][2][0],ut.STORE_ITENS[item][2][1])
            itens.append(Item(item, amount, price))
        return itens

    def validate_purchase(self, money, item):
        if money - item.get_value() >= 0:
            return True
        return False

    def apply_discount(self, discount, winner):
        for item in self.itens:
            if winner == 1: item.price += discount[0]
            else: item.price -= discount[1]
