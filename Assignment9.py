#Ques 1
#Name of the exception is ZeroDivisionError
a=3
if(a<4):
    try:
        a=a/(a-3)
        print(a)
    except:
        print("Division by zero not allowed")


#Ques 2
#Name of the exception is IndexError
l=[1,2,3]
try:
    print(l[3])
except:
    print("Index out of range")


#Ques 3
#NameError: Hi there


#Ques 4
# -5.0
#"a/b result in 0"


#Ques 5

#1. ImportError: Occurs when we try to import a module that doesn't exist in system path
try:
    import abcd
except ImportError:
    print("Module not found")

#2. ValueError:
try:
    print(int('Hello'))
except ValueError:
    print("Value Error")

#3. IndexError:
l=[1,2,3]
try:
    print(l[3])
except IndexError:
    print("Index out of range")
