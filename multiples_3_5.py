#Function to print the sum of multiples of 3 and 5 for given argument limit

def multiple(limit):
    sum=0
    for i in range(0,limit+1):
        if i%3==0:
            sum+=i
        elif i%5==0:
            sum+=i
    print(sum,"is the multiple of 3 and 5")
multiple(100)
