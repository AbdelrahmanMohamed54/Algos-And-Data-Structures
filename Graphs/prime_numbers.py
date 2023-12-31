# Get primes in interval [2, n)
def get_primes_in_interval_naive(n):
    for i in range(2, n):
        if is_prime_naive(i):
            yield i


def is_prime_naive(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True


def get_primes_in_interval_faster(n):
    for i in range(2, n):
        if is_prime_faster(i):
            yield i


def is_prime_faster(n):
    i = 2
    while i*i <= n:
        if n%i == 0:
            return False
        i += 1
    return True


def get_primes_in_interval_new(n):
    is_prime = [False, False] + (n-2) * [True]
    for i in range(2, n):
        if is_prime[i]:
            yield i
            for j in range(2*i, n, i):
                is_prime[j] = False


def get_primes_in_interval_sieve(n):
    is_prime = [False, False] + (n-2) * [True]
    i = 2
    while i*i <= n:
        if is_prime[i]:
            for j in range(i*i, n, i):
                is_prime[j] = False
        i += 1
    for i in range(n):
        if is_prime[i]:
            yield i
