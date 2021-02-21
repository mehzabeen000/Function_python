#Function to check the even numbers of same position in the list.
def check_numbers_list(num1,num2):
    for i in range(0,len(num1)):
        if num1[i]%2==0 and num2[i]%2==0:
            print("Both are even number")
        else:
            print("Both are not even number")
check_numbers_list([20,30,40,12],[12,14,17,19])
    

