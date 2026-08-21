#4.Prime or Not Prime:
def PrimeOrNotPrime(num):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return "Not Prime"
        return "Prime"
    return "Not Prime"

num = int(input("Enter a number: "))
print(PrimeOrNotPrime(num))

#2.find all prime numbers in a given range
def find_primes(start, end):
    for num in range(start, end + 1):
        if num > 1:
            is_prime = True

            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break

start = int(input("Enter start: "))
end = int(input("Enter end: "))

print(find_primes(start, end))


#3.sum of all prime numbers in a given range

start = int(input("Enter start range: "))
end = int(input("Enter end range: "))

prime_sum = 0

for num in range(start, end + 1):
    if num > 1:
        is_prime = True

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            prime_sum += num

print("Sum of prime numbers =", prime_sum)