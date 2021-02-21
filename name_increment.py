#Function to print the following pattern (Mehzabeen = M_ Ee_ Hhh_ Zzzz_ Aaaaa_ Bbbbbb_ Eeeeeee_ Eeeeeeee_ Nnnnnnnnn)
def user(name):
    j=1
    b=''
    for i in name:
        a=i*j
        b=b+a+'_'
        j+=1
    b=b[:-1]
    i=0
    while i<len(b): 
        if b[i]=='_':
            i+=1
            print('_',b[i].upper(),end='')
        else:
            print(b[i],end='')
        i+=1
user("Mehzabeen")
