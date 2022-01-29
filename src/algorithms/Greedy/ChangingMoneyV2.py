class ChangingMoneyV2(object):
    @staticmethod
    def change(number, coins):
        size = len(coins)
        number_coins = 0

        for i in range(0, size):
            result = int(number / coins[i])
            number_coins = number_coins + result
            if result > 0:
                number = number - (result * coins[i])

        return number_coins
