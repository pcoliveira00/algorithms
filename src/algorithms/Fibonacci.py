import numpy as np


class Fibonacci(object):

    @staticmethod
    def fib(n):
        array = np.zeros(n+1)
        array[0] = 0
        array[1] = 1

        for i in range(2, n+1):
            s = array[i-1] + array[i-2]
            array[i] = s

        return array[n]
