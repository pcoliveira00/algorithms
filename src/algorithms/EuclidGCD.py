class EuclidGCD(object):

    @staticmethod
    def gcd(a, b):
        if b == 0:
            return a

        a_remainder = a % b

        return EuclidGCD.gcd(b, a_remainder)
