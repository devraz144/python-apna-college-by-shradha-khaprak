  # FUNCTION -> blocks of statement that performs a specefic task
  # function take input know as parameters and return output 

  #defination

'''

def sum(a , b):  # function defination , function parameters

    s= a+b
    print( s)
    return s

sum(12,33)    # funtion call ,function argument 

'''

'''

def pr():
    print("nothing")

print(pr()) // output will be   None

'''

# type of function 
 # 1. -> build-in functions -> len() , print() , type(), range()
 # 2. -> user defined functions

 # default parameters  -> assigning a default value to parameter, which is used when no argument is passed 
 # default values are given from last to first likelyy understand 

'''

def cal( a = 12 , b= 22):
    return a*b

print( cal(2) )

'''

#let's practice 

# 1. waf to print the length of the list .( list is the paramerter)

'''

list1 = [1,2,3,4]

def cal ( l1):
    return (len(l1))

print(cal(list1))

'''

# 2. waf to print the elements of a list in single line . ( list the parameter)

'''

list1=[1,3,4,5]

def cal(l1):
    for i in l1:
        print(i,end=" ")

cal(list1)

'''

#3. wap to find the factorial of n ( n is the parameter)

''' 

n = int ( input("enter the number "))

def cal(n):
    ans = 1
    for i in range(n,1,-1):
        ans=ans*i
    print(ans)

cal(n)

'''


   ### RECURSION -> when a function call itself 

# stopping condition is known here as base condition 

# working -> call stack 

#let's practice

# 1.-> write a recursive function to calculate the sum of first n natural number 

'''

def cal ( n  ):
    if(n==0):
        return n
    
    return cal(n-1) + n


print(cal(4))

'''
