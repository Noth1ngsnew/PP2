is_prime = lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1))

k=input()
numbers=list(map(int,k.split()))

prime_numbers = list(filter(is_prime, numbers))

print("Простые числа:", prime_numbers)
