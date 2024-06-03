def is_prime(number):
    trigger = True
    prime_list=[]
    if number > 1 :
        for i in range (2,number):
            if number % i == 0 :
                trigger = False
                # le nombre est divisible ; non premier                
                break
            else :
                trigger = True
                # le nombre est premier
        if trigger == True :
            prime_list.append(number)
    elif number <= 1  :
        trigger = False
        
    print (prime_list)


"""
REMEMBER !!!!!!!
Write a program that prints all prime numbers. (Note: if your programming language does not support arbitrary size numbers, printing all primes up to the largest number you can easily represent is fine too.)
"""

for j in range (2,1000):
    is_prime(j)
