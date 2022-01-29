class ChangingMoney(object):

    @staticmethod
    def change(number, coins):

        size = len(coins)

        if number == 0:
            return 0

        number_coins = 0
        for i in range(0, size):
            while number >= coins[i]:
                number = number - coins[i]
                number_coins = number_coins + 1

        return number_coins
