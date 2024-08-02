# OOP IN PYTHON -> to map with real world scenariors we used to deal with object 
 # this is known as object oriented programming

# by the redundancy decreases and reuseablity increase 

# class is the blueprint for creating object

# creating class 

'''

class student:
    name = "devraj"

c1 = student()
print(c1.name)

'''

## __init__ function -> constructor
## self is the first parameter of the function  in the class 

'''

important 


class car :
    colour = 233
    def __init__(self,name):
        self.name= name
        print("go")

r1 = car("dev")
print(r1.name)

'''

# the self is the parameter is a reference to the current instance 
# of the class , and is used to access variables that belongs to the class

# it is also like this of c++ 

# variable of the class -> attributes 

# default constructor 
# parametrized constructor 

# class atribures -> that is same for every object 
# object attributes -> that is different for every object and made by self 

# -> precedance order -> object att > class att ( if their vairable name is same )


# method  -> function 

# attribute can be changed by also [ s.name = " devraj " ]

# static method -> that dont use the self parameter( work at class level) and same for evry object 



''' 
 class student : 
    @staticmethod  #also known as decorator
    def colleage():
        print("abc college")

'''

# 1. abstraction  -> hiding the implemetation detail of the class and only showing the essential feature to the user 
# 2. encapsulation ->wrappping data and fuction into a single unit ( object )