class Coin_game:
    def __init__(self, qtdMoedas, retira1, retira2, discount):
        self.qtdMoedas = qtdMoedas
        self.retira1 = retira1
        self.retira2 = retira2
        self.player = 1
        self.discount = discount
        self.memoization = self.play_challenge()

    def play_challenge(self):
        memoization = [0 for i in range(self.qtdMoedas+1)]
        memoization[0] = False
        memoization[1] = True

        for i in range(2, self.qtdMoedas+1):
            if (i - 1 >= 0 and not memoization[i - 1]): memoization[i] = True
            elif (i - self.retira1 >= 0 and not memoization[i - self.retira1]): memoization[i] = True
            elif (i - self.retira2 >= 0 and not memoization[i - self.retira2]): memoization[i] = True
            else: memoization[i] = False

        return memoization

    def calculate_move(self):
        if not self.memoization[self.qtdMoedas - self.retira1] and self.qtdMoedas - self.retira1 >= 0: return self.retira1
        elif not self.memoization[self.qtdMoedas - self.retira2] and self.qtdMoedas - self.retira2 >= 0: return self.retira2
        elif self.qtdMoedas - 1 >= 0: return 1
