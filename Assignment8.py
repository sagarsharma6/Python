#Ques 1

class circle:
    def __init__(self):
        self.rad=5
    def area(self):
        area=3.14*self.rad*self.rad
        print("Area is:",area)
    def cir(self):
        cir=2*3.14*self.rad
        print("Circumference is:",cir)
obj=circle()
obj.area()
obj.cir()


#Ques 2

class student:
    age=0
    marks=0
    def __init__(self):
        self.name='abc'
        self.roll=33
    def setAge(self):
        self.age=20
    def setMarks(self):
        self.marks=90
    def display(self):
        print("Name= {}\nroll no= {}\nage= {}\nmarks= {}".format(self.name,self.roll,self.age,self.marks))
obj=student()
obj.setAge()
obj.setMarks()
obj.display()


#Ques 3

class Temp:
    def convertCelsius(self):
        fah=float(input("Enter temp in fahrenheit: "))
        cel=(fah-32)/1.8
        print("Temperature in celsius is:",cel)
    def convertFahrenheit(self):
        cel=float(input("Enter temp in celsius: "))
        fah=cel*1.8+32
        print("Temperature in Fahrenheit is:",fah)
obj=Temp()
obj.convertCelsius()
obj.convertFahrenheit()


#Ques 4

class MovieDetails:
    profit=0
    def __init__(self):
        self.artist="ABC"
        self.yor=2014
        self.ratings=8.8
    def display(self):
        print("Artist Name= {}\nYear of Release= {}\nRatings={}\nProfit= {}".format(self.artist,self.yor,self.ratings,self.profit))
    def  add(self):
        self.profit="$4.4 Million"
obj=MovieDetails()
obj.add()
obj.display()


#Ques 5

class animal:
    def animal_attributes(self):
        s_name="Panthera tigris"
        weight=600
        claws=4
        canines=3
        print("Scientific Name= {}\nWeight= {}\nClaws= {} inch\nCanines= {} inch".format(s_name,weight,claws,canines))
class tiger(animal):
    pass
obj=tiger()
obj.animal_attributes()


#Ques 6

class A:
    def f(self):
        return self.g()
    def g(self):
        return 'A'
class B(A):
    def g(self):
        return 'B'
a = A()
b = B()
print(a.f(), b.f())
print(a.g(), b.g())


#Ques 7

class shape:
    def __init__(self):
        self.len=int(input("Enter length: "))
        self.bre=int(input("Enter bredth: "))
    def area(self):
        area=self.len*self.bre
        print("Area is",area)
class rectangle(shape):
    def __init__(self):                             #Method overriding
        print("Rectangle:")
        super().__init__()                          #calls the base class constructor so as to define variables len and bre
class square(shape):
    def __init__(self):
        print("Square:")
        super().__init__()
obj1=rectangle()
obj1.area()
obj2=square()
obj2.area()
