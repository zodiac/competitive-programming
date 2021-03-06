#!/usr/bin/env python3

import array

def make_nCr_mod(max_n=2 * 10**5, mod=10**9 + 7):
    fact, inv_fact = [0] * (max_n + 1), [0] * (max_n + 1)
    fact[0] = 1
    for i in range(max_n):
        fact[i + 1] = fact[i] * (i + 1) % mod

    inv_fact[-1] = pow(fact[-1], mod - 2, mod)
    for i in reversed(range(max_n)):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod

    def nCr_mod(n, r):
        res = 1
        while n or r:
            a, b = n % mod, r % mod
            if a < b:
                return 0
            res = res * fact[a] % mod * inv_fact[b] % mod * inv_fact[a - b] % mod
            n //= mod
            r //= mod
        return res

    return nCr_mod

nCr_mod = make_nCr_mod()

T = int(input())

ans = array.array('i', [1]*(10**5+1))

for n in range(2,len(ans)):
    spots = 2*(n-1)+1
    ans[n] = ans[n-1]*(nCr_mod(spots,2)+spots) % (10**9 + 7)

for _ in range(T):
    N = int(input())
    print(ans[N])