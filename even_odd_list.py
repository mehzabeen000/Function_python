#we have to print the odd and even list from the given list without using if_else

num=[1,2,3,4,5,6,7,8,9,10]
even=list(filter(lambda a:a%2==0,num))
print(even)
odd=list(filter(lambda b:b%2==1,num))
print(odd)