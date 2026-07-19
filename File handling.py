#File Handling:

for example: I created a file called "fruits" (txt file), inside it i stored apple, orange, banana. i need to open this file through file handling, lets see how to do!

f=open("fruits.txt")
#to read the file
content=f.read()  #just give the details of this file  
print(content)  #it shows actually what inside that file. output: apple, orange, banana.

#to write the file: first, we have to change the mode as 'r' to 'w' and when we write anything using write() inside the file, we should close() then only the written will show but the existing contents are deleted, and only it shows the current written contents.
f=open("fruits.txt","w")
f.write("grape\n")
f.write("lichi")
f.close()
#OUTPUT: 
grape
lichi
---
#To again read or see the contents of the file:
f=open("fruits.txt","r+")
print(f.read()) #output: grape, lichi
---
#append
f=open("fruits.txt","a")
f.write("apple\n")
f.write("orange\n")
f.close()

f=open("fruits.txt","r+")
print(f.read())
#output:
grape
lichi
apple
orange

#and, if we use print(f.radline()) - readlie, it prints the contents one by one.
