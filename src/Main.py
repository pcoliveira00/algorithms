from src.algorithms.QuickFind import QuickFind
from src.algorithms.QuickUnion import QuickUnion
from src.algorithms.BinarySearch import BinarySearch
from src.algorithms.NaiveFibonacci import NaiveFibonacci
from src.algorithms.Fibonacci import Fibonacci
from src.algorithms.NaiveGCD import NaiveGCD
from src.algorithms.EuclidGCD import EuclidGCD
from src.algorithms.Greedy.ChangingMoney import ChangingMoney
from src.algorithms.Greedy.ChangingMoneyV2 import ChangingMoneyV2

import time

# inputs = input("Inform the nodes array:")

"""
qf = QuickFind(inputs)

qf.union(0, 1)

print(qf.connected(0, 1))

print(qf.elements)

qu = QuickUnion(inputs)

qu.union(0, 1)

print(qu.connected(0, 1))

print(qu.elements)




bs = BinarySearch(inputs)
key = int(input("Key to be searched?"))
print(bs.find(key))



stack = Stack()

string_inputs = input("Type the elements in the stack")

string_array = []

for i in inputs.split(' '):
    if i == '-':
        stack.pop()
    else:
        stack.push(i)


n = 1000

print("Naive Fibonacci")
start = time.process_time()
print(NaiveFibonacci.fib(n))
end = time.process_time()

print(end - start)

print("Fibonacci")
start = time.process_time()
print(Fibonacci.fib(n))
end = time.process_time()

print(end - start)


a = 155555534343430
b = 555555553434350

print(NaiveGCD.gcd(a, b))

print(EuclidGCD.gcd(a, b))
"""

coins = [10, 5, 1]

print("N**2")
start = time.process_time()
print(ChangingMoney.change(99708064, coins))
end = time.process_time()
print(end - start)

print("N")
start = time.process_time()
print(ChangingMoneyV2.change(99708073, coins))
end = time.process_time()
print(end - start)

