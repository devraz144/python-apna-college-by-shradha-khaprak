          ## file i/0 in python 
# python can be used to perform operation on a file . ( read & write data )

# ram are  varstile so we don't store things in ram .  while we store things in file 
# so that we can have that for long period of time 


# major operation 

# 1. -> how to open a file 
# 2. -> how to read a file
# 3. -> how to write in a file
# 4. -> how to close a file 
# 5. -> how to delete a file 


# type of all file 

#1. text file : .txt , .docx , .log etc in which data are stored in charcter format 
#2. binary file : .mp4, .mov , .png , .jpeg etc  in which data are not stored in character format 

# we can access all file through python 

# for open 

# open("file_name " , " mode ") it return stream and by default mode is of read and if we do any write on this then it will give us an error 

'''

f = open("lec7.txt","r")
data = f.read()
print(data)
f.close 

'''


'''

char                    meaning 
'r'          open for reading(default)
'w'          open for writing but it delete all the thing that file had 
'x'          create a  new file and open it for writing
'a'          open for writitn and appending to the end of the file if it exists
'b'          binary mode we have write --> open("file_name","mode_b)
't           textmode(default)
'+'          open a disk file for updating (reading and writing )


'''

# ---> imp imp -> cursol don't go back <---- imp imp 

# reading a file 

'''

data=f.read() // read entire file
data =f.read(19) // read first 19 charcter only 
data=f.readline()// read one line at a time 

'''

# writing to a file 

# additonal tip go for an random artice to read on file of python 

# if file name is not been found in [w] and [a] then it will create a new file with that name 

'''

f = open("lec7.txt","w")
f.write( "here i start the next thing also")

'''

'''

f = open("lec7.txt","a")
f.write("\n i can also write new new things in python ")

'''

# there aslo new thing like r+ , w+ , a+ 

# r+ -> read and write and  the data will not delete from that 
# -> it also overwrite and start writing from the beginign of the file 

# w+ -> read and write , the data will be deleted
# -> all thing that we will write wiil be written after deleteing all the text 

# a+ -> read and write allow and work as a simple append 
# -> ptr at always last 

  ###  with syntax 

'''

with open("file_name","method") as f :
    data=f.read()

''' 

# it has indendent it will all depenend upon f 
# file will be automatically close 

   ### deleting a file 

# module ( like a code libary ) is a file wrirtten by anothe programmer that 
# genrally has a function that we can use 

# using the os modle

'''

import os 
os.remove(file_name)

'''

# pip -> package installer for python 
# pip install package_name
# if pip not work pip3 will then 


#   LETS PRACTICE QUESTION 


