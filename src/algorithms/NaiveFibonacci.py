class NaiveFibonacci(object):
    @staticmethod
    def fib(n):
        if n <= 1:
            return n
        else:
            return NaiveFibonacci.fib(n - 1) + NaiveFibonacci.fib(n - 2)
