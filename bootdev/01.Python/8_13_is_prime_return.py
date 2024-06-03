def is_prime(number):
    if number > 1 :
        trigger = True
        for i in range (2,number):
            if number % i == 0 :
                trigger = False
                break
            else :
                trigger = True  
        return trigger
    elif number <= 1  :
        trigger = False
        return trigger

primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
for i in primes :
    is_prime(i)

print (type(primes))
# <class 'tuple'>