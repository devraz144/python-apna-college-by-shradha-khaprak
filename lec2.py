#string's index cant be changed while whole string can be changed 

#escape sequence character 
# 1. next line -> \n
# 2. tab ->\t

# method on string 
#1. concatnation -> using + sign  it is used to add to string 
#2. len(string1) -> it find the length of the string and also whitsapce are also included in it 


'''str1 = "dev "
print("str1 is " , str1)
str2 ="raj "
print( "str2 is ",str2)
print( "the length of the strq1 is ",len(str1) , "\nthe length of the str2 is ", len(str2))
str3= str1+str2+"sharma"
print("str3:", str3)
print("the length of the str3 is " ,len(str3))'''

#3.sliceing 

# syntax -> 1. str[starting_index : ending_index] but ending index are never included in this slice  2. str[ : ending index ] at blank there is 0 
# 3. str[starting index : ] at blank ther is len(str)  

# imp ( python also offers negative indexing in string and we can aslo use slicing in negative index)
#  A  P  P  L  E 
# -5 -4 -3 -2 -1
# str[-5 , -1] // it will return APPE        


# FUNCTION  -> they dont make change in orginal string 

'''
str1 ="dev" 
print(str1.replace("e","r"))
print(str1)
'''

#1. str.endswith("word") it return true if it end with word otherwise it return false 
#2. str.capitalize()  -> capital the first word of the string but didnt maek change in orgianl string 
#3. str.replace("a", "b") -> inside the string a will be replaced by b 
#4. str.count("a") -> it will count the no of a in the string
#5. str.find("word") -> it return the first index of the word if not exixt the it return -1



#conditional state 

'''
if(cond):
    statement 1
elif(cond):
    statement 2
else: 
    conditon 3
the space is of 4 or of tab okay  and is known as indentation 
'''

#if is always checked but elif is checked when the above condition is falsed 

#nesting is also vaild in python 

#lets pracitce 
#1. wap to check if a number by the user is odd or evev
#2. wap to find the greatesst of 3 numbers entered by the user 
#3. wap to check if a number is a mutliple of 7 or not 



