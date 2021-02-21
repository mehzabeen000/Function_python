#Function to print even and odd number 
def showNumbers(limit):
    for i in range(0,limit+1):
        if i%2==0:
            print("Even =",i)
        else:
            print("odd =",i)
showNumbers(100)
