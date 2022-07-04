#!/usr/bin/env python
# Fibonacchi implementation using Recursion
# fibo(n) is the nth value of the sequence
# fibo(n) calculates the nth value

def fibo(n):

    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return (fibo(n-1) + fibo(n-2))


for i in range(5):
    print(fibo(i), end=" ")
