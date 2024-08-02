     ### DICTIONARY IN PYTHON ###

# dicationary are likely to js's object . it is used to store the key: value pairs 
# they are unoredered , mutable(changeable) and don't allow duplicate keys

''' 
dict = {
   "name" : "devraj"
   "cgpa" : 7.0 
   "here can be tuple" : "bcoz key must be fixed can be integer float "
   " here can't be list " : " bcoz list is changeable "
   " here can be integer " : " as it is alwayas fixed "
   
}

'''

# to access any vlaue we can write -> dict["key"] 
# to assign -> dict["key"] = " value "
# to make new key value -> dict["new_key"] ="new_value"

# to create NULL dict -> dict={}
# nested dictionary is also allowed . vlaue can be of dictonary

# to access nested value -> dict["key"]["nested_key"] 

# dictionary method 

# 1. -> dict.keys() // return all keys
# 2. -> dict.values() // return all vlaue 
# 3. -> dict.items() // return all the(KEY , VALUE)  pair in format of tuple 
# 4. -> dict.get("key") // return the value if present . if not present then it will not give us any error 
# 5. -> dict.update(newdict) // insert the specifed item to the dictionary and newdict must be a dictionary 


# typecasting is also possible 
# list(list) , tuple(list) , and so many 

        ### SET IN PYTHON 

# set is the collection of unordered items
# each elemetn in the set must be unique and immutable (can't be changed )

# boolean , int , float , string , tuple can be stored in set 
# bcoz above of these are immutable in python (can't be changed )

# list and dict cant be stored bcoz they are mutable and set is immutable 

# declaration  -> collection = { 1,2,3,4,5}
# it ignores the duplicate vlaue but not throw any kind of error

# repeated elements are stored only once 

# collection = {}  // it it empty dictionary
# collection = set()  // it is empty set 

# set-> mutable
# set-> elements -> immutable 

# hashable -> for immutable thing -> that can't be changed
# unshasable -> for mutable thing -> the values theat can be change 

#method in set 

# 1. set.add(vlaue ) // it add element 
# 2. set.remove(el)  // it remvove that elemetn . if not present then be ready for error
# 3. set.clear() // empites the set 
# 4. set.pop() // remove any random vlaue , can be used to generate a random vlaue 

# 5. set.union(set2) // combine both set vlaue and return new and set1 , and set2 still have its orginal value 
# 6. set.intersection(set2) // combine common elemnent and return new .set1 and set2 still have its orginal value

# let's practice 

# 1. -> store the following word meannng in a python dict 

 # table : " a piece of furnitur", "listof ffacts & figures "
 # cat " a small animal "

'''

dict={}
dict["table"]=[ " a piece of furnitur", "listof ffacts & figures "]
dict["cat"]="a small animal"
print(dict)

'''

#2. second one go to slide notes of apna colleage 
#3.  like 2 
#4. figure out a way to store 9 and 9.0 as separate value in the set  ( u can take help of buit-in data type )

'''

# as an string 
vlues={9 ,"9.0"}
print(vlues)

# as an key and value but not as a dictionary

values = {
    ("float",9.0),
    ("int", 9)
}
print(values)

'''






