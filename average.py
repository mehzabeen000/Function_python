#Function to print the average numbers
def avg_sum():
    number=int(input("How many count of number you want to average? Enter:/n"))
    sum=0
    for i in range(number):
        num=int(input("Enter the number"))
        sum+=num
    print((sum//number, "is the average of", number,"element"))
avg_sum()
