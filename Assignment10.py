#Ques 1

f=open('test.txt')
n=int(input("How many lines you want to read: "))
for i in range(n):
    print(f.readline(),end='')
f.close()


#Ques 2

f=open('test1.txt')
read=f.readlines()
string=''.join(read)
string1=string+' '
count=1
for i in range(len(string)):
    if(string[i]==' ' or string[i]=='\n'):
        if(string1[i+1]!=' ' and string1[i+1]!='\n'):
            count+=1
print("Frequency of words is:",count)
f.close()


#Ques 3

f=open('test2.txt')
g=open('test3.txt','w')
g.write(f.read())
g.close()
f.close()


#Ques 4

f=open('test2.txt')
g=open('test3.txt')
for i in f:
    print(i.strip()+g.readline())


#Ques 5

f=open('test4.txt')
my_list=f.readlines()
my_list=[int(i.strip()) for i in my_list]
my_list.sort()
my_list2=[]
for i in my_list:
    my_list2.append(str(i))
my_str='\n'.join((my_list2))
g=open('test5.txt','w')
g.write(my_str)
g.close()
f.close()
