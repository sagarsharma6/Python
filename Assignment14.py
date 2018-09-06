#Ques 1

l=[1,2,3,4,5]
new_l=[x**3 for x in l]
print(new_l)


#Ques 2

prime=[x for x in range(1,50) if all(x%y!=0 for y in range(2,x//2+1))]
print(prime)


#Ques 3

#Main differences between list comprehension and generator expression
#1. In list comprehension a <class list> object is returned whereas in generator expression a <class generator> object is returned.
#2. Genereator expression takes less memory.


#LAMBDA AND MAP
#Ques 1

celsius=[39.2,36.5,37.3,37.8]
result=list(map(lambda x:float(9/5)*x+32,celsius))
print(result)


#Ques 2

l=[1,2,3,4,5,6]
new_l=list(map(lambda x:x**2,l))
print(new_l)
    
#FILTER AND REDUCE
#Ques 1
def chk_prime(n):
    for i in range(2,n//2+1):
        if(n%i==0):
            return False
    else:
        return True
prime_list=list(filter(chk_prime,range(1,50)))
print(prime_list)


#Ques 2

from functools import reduce
lst=[1,2,3,4,5,6]
print(reduce(lambda x,y:x*y,lst))
