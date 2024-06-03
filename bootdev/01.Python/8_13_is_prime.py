def is_prime(number):
    if number > 1 :
        trigger = True
        for i in range (2,number):
            if number % i == 0 :
                trigger = False
                # print (False)
                break
            else :
                trigger = True  
                # print (True)
        print(f"the number {number} is prime : {trigger}")
    elif number <= 1  :
        trigger = False
        print(f"the number {number} is prime : {trigger}")

primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
for i in primes :
    is_prime(i)


"""
REMEMBER !!!!!!!
Write a program that prints all prime numbers. (Note: if your programming language does not support arbitrary size numbers, printing all primes up to the largest number you can easily represent is fine too.)
"""

for j in range (2,1000):
    is_prime(j)
