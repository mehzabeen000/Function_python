#we have to make one function of calculator
def calculator(num1,operator,num2):
    if operator=="+":
        print(num1+num2)
    elif operator=="-":
        print(num1-num2)
    elif operator=="*":
        print(num1*num2)
    elif operator=="/":
        print(num1/num2)
calculator(5,"*",3)


def multiply(list1,list2):
    for i in range(0,len(list1)):
        print(list1[i]*list2[i])
multiply([1,2,3,4],[10,20,30,40])


    