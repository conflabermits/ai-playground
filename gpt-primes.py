#!/usr/bin/env python3

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def generate_primes(n):
    primes = []
    for i in range(2, n+1):
        if is_prime(i):
            primes.append(i)
    return primes

n = int(input("Enter the value of n: "))
print("Prime numbers upto", n, "are:", generate_primes(n))

