def divisors(integer):
    divisors = []
    for i in range(2, integer):
        if integer % i == 0:
            divisors.append(i)
    return f'{integer} is prime' if len(divisors) == 0 else divisors