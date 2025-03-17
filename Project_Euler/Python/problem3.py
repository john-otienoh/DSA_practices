import math

def largest_prime_factor(n: int) -> tuple[int, list]:
    """
    Returns a list of the prime factors and 
    the largest prime factors of an integer
    """
    factors = []
    while n % 2 == 0:
        n /= 2
    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0:
            factors.append(i)
            n /= i
    return max(factors), factors

if "__main__" ==__name__:
    num = int(input("Enter a number: "))
    m, f = largest_prime_factor(num)
    print(f"The list of prime factors for {num} is {f}.")
    print(f"The largest prime factor of the number {num} is {m}.")
