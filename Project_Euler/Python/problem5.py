def smallest_multiple(n: int) -> bool:
    """
    Return smallest positive number 
    that is evenly divisible by all of the numbers from 1 to 20.
    """
    values = set()
    for i in range(1, 21):
        if n % i == 0:
            values.add(True)
        else:
            values.add(False)
    if len(values) == 1:
        return True
    else:
        return False

for i in range(1, 10000):
    if (smallest_multiple(i)):
        print(i)
