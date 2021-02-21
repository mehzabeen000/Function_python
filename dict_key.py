#Function to print the number and square of the number in dictionary according to the argument.

def dict_key(num):
    num_squares=0
    dict={}
    for i in range(1,num+1):
        num_squares=i*i
        dict[i]=num_squares
    print(dict)
dict_key(10)
