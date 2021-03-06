#!/usr/bin/env pypy3

import math

class Sieve:
    def __init__(self, n=10**7+100):
        self.N = n

        s = [-1] * n
        for i in range(2, int(n**0.5)+1):
            if s[i] != -1: continue
            for j in range(i, n, i): 
                if j > i: s[j] = i
        self.s = s

        self.PRIMES = self.primes()
        # print(len(self.PRIMES))
    
    def primes(self):
        return [i for i, e in enumerate(self.s) if e == -1 and i >= 2]

    def fastfactorize(self, n):
        assert(n <= self.N)

        ret = []

        while self.s[n] != -1:
            ret += [self.s[n]]
            n = n // self.s[n]

        ret += [n]

        return ret

    def isprime(self, n):
        if n < self.N:
            return self.s[n] == -1
        for p in self.PRIMES:
            if p*p > n:
                return True
            if n % p == 0:
                return False

    def factorize(self, n):
        if n < self.N:
            return self.fastfactorize(n)
        
        for p in self.PRIMES:
            if p*p > n:
                break
            if n % p == 0:
                return [p] + self.factorize(n // p)

        return [n]

sieve = Sieve(10**3)

PRIMES = sieve.PRIMES

def ok(P):
    if P == 2: return False

    for i in range(len(PRIMES)-1):
        if PRIMES[i] + PRIMES[i+1] + 1 == P: return True

    return False

def count(N):
    c = 0
    for p in PRIMES:
        if p not in range(2,N+1): continue
        if ok(p): c += 1
    return c

def ans(N, K):
    if count(N) >= K:
        return "YES"
    return "NO"

N, K = input().split(' ')
N = int(N)
K = int(K)

print(ans(N, K))
