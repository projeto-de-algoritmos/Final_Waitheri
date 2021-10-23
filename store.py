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
    #TODO: a princípio o discount é uma tupla (desconto se vitória, aumento se perda)
    def __init__(self, discount):
        self.itens = self.__init_itens()
        self.discount = discount
        # already_player é para evitar que ele fique pedindo descontos
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

    #TODO: lembrar de subtrair o valor no app e aplicar o efeito do item
    def validate_purchase(self, money, item):
        if money - item.get_value() >= 0:
            return True
        return False

    def apply_discount(self, winner):
        for item in self.itens:
            if winner == 1: item.price -= self.dicount[0]
            else: item.price += self.discount[1]

    def play_challenge(self, qtdMoedas, retira1, retira2):
        memoization = [0 for i in range(qtdMoedas+1)]
        memoization[0] = False
        memoization[1] = True

        for i in range(2, qtdMoedas+1):
            if (i - 1 >= 0 and not memoization[i - 1]): memoization[i] = True
            elif (i - retira1 >= 0 and not memoization[i - retira1]): memoization[i] = True
            elif (i - retira2 >= 0 and not memoization[i - retira2]): memoization[i] = True
            else: memoization[i] = False

        return memoization
