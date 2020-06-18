def get_prime_factors(N):
    prime_factors = []
    divisor = 2

    while (divisor<=N):
        if (N % divisor) == 0:
            prime_factors.append(divisor)
            N = N/divisor
        else:
            divisor += 1
    
    return prime_factors
