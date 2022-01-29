class NaiveGCD(object):
    @staticmethod
    def gcd(a, b):
        best = 0
        for number in range(1, a + b):
            if a % number == 0 and b % number == 0:
                best = number
        return best
