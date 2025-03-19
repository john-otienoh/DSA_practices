def prime_number(n: int) -> bool:
    """check if a number is a prime number"""
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def nth_prime_number(n: int) -> int:
    count, prime_nums = 3, [2]
    while len(prime_nums) < n:
        if prime_number(count):
            prime_nums.append(count)
        count += 2
    return prime_nums[-1]

if "__main__" == __name__:
    num = int(input("Enter a number: "))
    l = nth_prime_number(num)
    # print(f"")
    print(f"{num} prime number is {l}")
