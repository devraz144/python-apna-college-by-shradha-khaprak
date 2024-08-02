   # loops are used to repet instructions

# 1. -> WHILE LOOPS 

'''
while condition :
    # code
'''

# iterator(i) and iteration ( how many time loops has run )
# infinite loop should not be there


#lets practice 

#1. print number from 0 to 100 
#2. print number from 100 to 0 
#3. print the multiplication table of n 
#4. print the elment of the list 
#5 .search for a number in the tuple using loop


# break & continue 

# break : used to terminate the loop when encountered 
# continue : terimate exexution in the current itereation & continue execution of the loop 
#            with the next iteration 

# continue : work as skip


#2. for loops 

'''

for el in list :
    // code 

'''


# for loop with else -> when the loop will end the else condition will be executed 
# if break is there in the loop and get executed then else conditon will not be executed 



''' 

# when the else condition will not exexuted 

str ="apnacolleage"

for i in str:
    if(i=="o"):
        print(" o has been found ")
        break :
else:
    print("end")

// output - apnac o has been found 

'''

''' 
# whent the else cond will executed 

str ="apnacolleage"

for i in str:
    if(i=="o"):
        print(" o has been found ")
        
else:
    print("END")

// output - apnac o has been found lleage END

'''

# pracice 
 # 1.-> print the elemetn of the list 
 # 2.-> find the element in the tupple


 #  range() -> range function return a sequence of number 
 # range(start? , stop , step?) // start and step are by default and can alos be given 


 # starting from 0 by default 
 # increament by 1 always
 # stops before a specifed number 

 # range(5) : start =0  : " end = 5 ": increament = 1 // output -> 0,1,2,34

'''

seq = range(5)

for i in seq:
    print(i)  # output ->0 ,1,2,3,4

'''


# pass statement 
# pass is the null statement that does nothing . it is used as a placeholder for futruer 


'''

for el in range():
    pass

print("good to go")

'''

# pass is used when you do not want to do anything in the block if not write this then it thorugh indentatioin error 


    
  