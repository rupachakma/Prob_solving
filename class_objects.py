
# OBJECTS:
# class MyClass:
#     height = 5.5
#     weight = 70
# x=MyClass()
# print(x.weight)
# MyClass.weight=20
# x=MyClass()
# print(x.weight)
# y=MyClass()
# print(y.height)
# x=MyClass()
# x.height = 4.5
# print(x.height)




#Q1= Write a class values have 3 variables like x,y,z.
#Q2= Create more than 2 objects of the class and print the objects own values.
#Q3 Than change the class variables default values permanantly.
#Q4 After changing the values please print these class atributes for one objects.

# class MyClass:
#     X=5
#     Y=3
#     Z=6
# ob1=MyClass()
# ob2=MyClass()
# ob3=MyClass()
# print(ob1.X,ob1.Y,ob1.Z)
# print(ob2.X,ob2.Y,ob2.Z)
# print(ob3.X,ob3.Y,ob3.Z)

# MyClass.X=20
# MyClass.Y=20
# MyClass.Z=20

# ob4=MyClass()
# print(ob4.X,ob4.Y,ob4.Z)



# class MyClass:
#     X=5
#     Y=3
#     Z=6
# ob1=MyClass()
# ob2=MyClass()
# ob3=MyClass()
# ob4=MyClass()


# MyClass.X=40

# ob1.X=20
# ob1.Y=12
# ob1.Z=15

# ob2.X='ab'
# ob2.Y='ac'
# ob2.Z='ad'

# ob3.X=4
# ob3.Y=2
# ob3.Z=1

# print(ob1.X,ob1.Y,ob1.Z)
# print(ob2.X,ob2.Y,ob2.Z)
# print(ob3.X,ob3.Y,ob3.Z)
# print(ob4.X,ob4.Y,ob4.Z)


# class Person:
#     def __init__(self,name,rupa):
#         self.n=name
#         self.r=rupa
       

#         print("hello",self.r)

#     def hi(self):
#         print(self.n)
        


# p1=Person("Wonder","world")
# p1.hi()
# ob1=Person("abc","This is Rupa")
# ob2=Person("abc","abcd")



# create a class
# take init method
# pass more than 2 arguments
# print the values another method
# create more than 2 objects and follow the above instruction


# class People:
#     def __init__(self,name1,name2,name3):
#         self.n1=name1
#         self.n2=name2
#         self.n3=name3
      

#     def Human(self):
#         print(self.n1,self.n2,self.n3)  

#     def Fruits(self):
#         print(self.n1,self.n2,self.n3)
    


# ob=People("Rahim","Karim","Rupa")
# ob.Human()
# ob2=People("Dhaka","Chittagong","Rangamati")
# ob2.Human()

# ob3=People("Water Melon","Mango","Orange")
# ob3.Fruits()



# class People:
#     def __init__(self,name,address,age):
#         self.n=name
#         self.a=address
#         self.ag=age
#     def abc(self):
#         print(self.n,self.a,self.ag)


# Rupa=People("Rupa","Rangamati",25)
# Rupa.abc()

# inheritance:

class Person:
    y = 20
class People:
    z = 30

class Student(Person,People):
    x = 10

class Rupa(Student):
    r = 100

class Office(Rupa,Student):
    o=50

object = Office()


print(object.x,object.y,object.z,object.r,object.o)
