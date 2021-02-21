#Program to print the prime number
def primeorNot(num):     
    for i in range(2,num):
        if (num % i) == 0:
            return False
            break
    else:
        return True
for j in range(1,1001):
    if primeorNot(j):
        print(j,"Prime number")
