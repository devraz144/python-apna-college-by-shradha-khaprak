# del keyword -> used to delete object or object_attributes

# object -> del object
# object -> del object.attributes

# private (like) attributes & method -> __attributesname -> underscore underscore
# def __hello():
#   print("hello")

# -> private att and method are meant to be used only within ther class and are not 
#   accessible form outside the class 

# 3. inheritance 

''' 
 
class car :
    /// code

class toyotacar(car):
    /// code

'''

# type of inheritance 

# single inheritance 
# multi level inheritance 
# multiple inheritance

'''

  class a:
    # code

  class b :
    # code
  
  class c (a,b):
    #code

'''

# super keyword = super().__init__(var1,var2 ....)

# to change in the static method 

# 1. classname.staticvar = value 
# 2. self.__class.staticvar = value 

# staticvar is that we want the change 
# and the value is what we want to assign 

'''

@ classmethod 
   def changename( cls , name ):
    cls.name = name 

'''

# classmethod have to be written 
# cls store the class reference 


# 1. static method 
# 2. class method 
# 3. instance method 

# property  -> it is the decorator on any method in the class to use the method as a property 

#1. claculting percantage on the threesubject 

class student :
    def __init__(self , phy , chem , math):
        self.phy = phy 
        self.chem =chem
        self.math = math

    def calPer(self):
        print( " the percantge is ", (self.phy+self.chem+self.math)/3)

s1 = student(89,78,89)
s1.calPer()
s1.phy = 98 
s1.calPer()


''' 

to remove this 
def calPer(self):
        print( " the percantge is ", (self.phy+self.chem+self.math)/3)

'''


'''

we instand can do 
  
  @property
  def percentage(self):
    return  (self.phy+self.chem+self.math)/3)

'''

# 4. polymorphism : operator oveloading 
# -> when the same operator is allowed to have different meaning according to the context 


# go and learn about dander function in python
# dander __add__ [only thing ]


