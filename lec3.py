# list is likely to be array  but not at all 

#declaration is below 

'''
mark= [12,21,423,64,76]
'''

# 1. indexing -> done 
# 2. print(list) -> done
# 3  type(list) -> done 
# 4. len(list) -> done
# 5. can store different type of data elemts also -> done 
#  example ''' student =["karna" , 89 , 78.0]
# 6. string is immutalbe means element access allowd and change was not allowed 
#    list is mutable means acces and change is also allowed 
# 7. concatiaton can also be done using  + operator 


# ->  slicing is also here  and negative index can also be used here 

# list_name[starting_index : ending_index] 
# list_name[ : ending_index] -> then starting_index is 0 
# list_name[starting_index: ] -> then ending index is len(list_name)

# list_method -> the changes that are made .are being made in the orignal list 

# 1. list.append(1) -> it will push 1 in the list 
# 2. list.sort( ) -> 1,2,3,4,5 
# 3. list.sort(reverse= True ) ->5,4,3,2,1
# 4. list.reverse() -> it will reverse the list 
# 5. list.insert(index, element )  -> insert element at specefix index
# 6. list.remove(element) -> list.remove(1) -> it will remove the first occurence of 1 in list 
# 7. list.pop(index) -> it will remove the element from the given index 
# 8. list.count(element) -> it count the no of the element in the given list 

 # tuple -> 
 # same as list but it is immutable like string 

# declaration --> marks = (1,3,52,4,3)
# elemetn can be accessed but cant not be changed like marks[0]=12 . it will through the error

# tup = (1) --> it will be treated as normal integer 
# tup= (1,)  --> as an tuple

# slicing like list and string 
# tup[1:4] --> 4'th index will not be included 

# list can be also stored in tupel 

#tuple method 
# 1. -> tup.index(el) -> it retrun index of first occurenece
# 2. -> tup.count(el) -> count total occurence of the el in tuple

'''

a = "devraj"
tup = (1,23,"324243",a)

'''



# lets practice

#1 . wap to ask to enter name of 3 fav movie and store them in list 

'''

a = input("enter the first movie \n")
b = input("enter the second moveie \n ")
c = input("enter the thrid movie \n ")
list1 = []
list1.append(a)
list1.append(b)
list1.append(c)
print(list1)

'''

#2. wap to check if a list contain a plaindrome oof elemnt or not ( hint: use copy() method )

'''

list1 = [1,3,3,1]
list2 = list1.copy()
list1.reverse()

if(list1==list2):
    print("it is palindrome ")
else:
    print("not a palindrome ")

'''



