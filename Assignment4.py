#Ques 1

my_list=[1,2,3,4,5,6]
my_list.reverse()
print(my_list)


#Ques 2

my_str="SaGaRsHaRmA"
for i in my_str:
    if(i.isupper()):
        print(i)


#Ques 3

my_str=input("Enter integers seperated with commas: ")
my_list=my_str.split(',')
for i in range(0,len(my_list)):
    my_list[i]=int(my_list[i])
print(my_list)


#Ques 4
my_str=input("Enter the string: ")
for i in range(0,len(my_str)):
    if(my_str[i]!=my_str[len(my_str)-1-i]):
        break;
print(i)
if(i==len(my_str)-1):
    print(my_str + " is palindromic")
else:
    print(my_str + " is not palindromic")

#Ques 5

import copy as c
my_list=[1,2,3,4,5,6,7]
my_list2=c.deepcopy(my_list)
print(my_list2)
#Difference between shallow copy and deep copy
#in shallow copy if a copy of list 1 is made in list 2 and we change the content of any list then that change is also reflected in the other list
#in deep copy if a copy of list 1 is made in list 2 and we change the content of any list then that change is not reflected in the other list
