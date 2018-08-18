#Ques 1
a=input("Enter string1: ")
b=input("Enter string2: ")
c=input("Enter string3: ")
my_list=[a,b,c]
print(my_list)

#Ques 2
my_list.extend(['google','apple','facebook','microsoft','tesla'])
print(my_list)

#Ques 3
my_list2=[1,2,3,1,4,2,5]
print("Count of obj 1: ",my_list2.count(1))

#Ques 4
my_list3=[5,4,3,2,1]
my_list3.sort()
print(my_list3)

#Ques 5
list1=[1,3,5,7]
list2=[2,4,6,8]
mylist=[]
mylist.extend(list1)
mylist.extend(list2)
mylist.sort()
print(mylist)

#Ques 6
my_list=[2,3,1,5,6,4,7,8,9]
even_count=0
odd_count=0
for i in my_list:
    if(i%2==0):
        even_count=even_count+1
    else:
        odd_count=odd_count+1
print("Count of even no:",even_count,"Count of odd no:",odd_count)
