import math
def sieve_of_Eratosthenes(n):
    """
    Return a list of all prime numbers less than or equal to n.

    Args:
    n (int): The upper bound of the range to check.

    Returns:
    list: A list of all prime numbers less than or equal to n.
    """
    # Initialize a list of all numbers from 0 to n
    numbers = [True] * (n + 1)

    # 0 and 1 are not prime numbers
    numbers[0] = numbers[1] = False

    # Loop through all numbers from 2 to sqrt(n)
    for i in range(2, int(math.sqrt(n)) + 1):
        # If i is prime, mark all multiples of i as not prime
        if numbers[i]:
            for j in range(i * i, n + 1, i):
                numbers[j] = False

    # Return all numbers that are still marked as prime
    return [i for i in range(n + 1) if numbers[i]]

def prime_text(n):
    return f"can be made with {n} pair(s) of primes:"
def main():
    n = int(input())
    nums = []
    for i in range(n):
        nums.append(int(input()))
    primes = sieve_of_Eratosthenes(max(nums))
    primes_set = set(primes)
    
    # lets find the prime additives
    for i, num in enumerate(nums):
        found_set = set()
        print_list = []
        for prime in primes:
            res = num - prime
            if res in primes_set and res not in found_set:
                found_set.add(prime)
                found_set.add(res)

                print_list.append(f"{prime}+{res}")
        print(f"{num} {prime_text(len(print_list))}")
        for  x in print_list:
            print(x)
        if i != n - 1:
            print()

main()
