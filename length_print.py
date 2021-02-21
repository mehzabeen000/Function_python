#function to print the greatest length string and if it is equal then print both.
def length_print(str1,str2):
    count_str1=0
    count_str2=0
    for i in str1:
        count_str1+=1    
    for i in str2:
        count_str2+=1
    if count_str1==count_str2:
        print(str1,str2)
    elif count_str1>count_str2:
        print(str1)
    else:
        print(str2)
length_print("Mehzabeen","Sheetal")
