numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for i in range(0, len(numbers)):
    if numbers[i] <= 1:
        continue
    else:
        for j in range(2, numbers[i]):
            if numbers[i] % j == 0:
                is_prime = False
                break
    if is_prime:
        primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])
    is_prime = True
print('Primes: ', primes)
print('Not primes: ', not_primes)
