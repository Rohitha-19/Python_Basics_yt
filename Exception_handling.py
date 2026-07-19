#Exception Handling/ Error Handling
Types:
 1. Compile Time Error
 2. Logical Error
 3. Runtime Error

1. Compile Time Error: (our mistake)
 - error occured while compiling
 Ex: print("Hello")  #Hello
     print("hi")     #hi
     printt("Welcome") #name_error occured 
like this, while compiling the program, the error occured id called compiling error.

2. Logical Error: (our mistake)
 - human mistake error
 Ex: a=1
     b=4
     print(b+b)  #8 
instead of, print(a+b), print(b+b) is given. this is called Logical Error.

3. Runtime Error:
  Ex: a=int(input())
      b=int(input())
      print(a+b)
if the user, put correct input like 12, 10, then the program works fine. but instead the user put a as 10 and b as hi, this occurs "value error". this is called runtime error.

To Prevent these, we can use try,except,finally in python. this is called "error handling"

#code 
    try:
       a=int(input())
       b=int(input())
       print(a+b)
    except Exception:
       print("Error")

---
    try:
       a=int(input())
       b=int(input())
       print(a+b)
    except Exception as e:  #this e denotes, what error occured in this program, in output screen.
       print("Error",e)
---
#finally keyword
    try:
       a=int(input())
       b=int(input())
       print("ADD:",a+b)
    except Exception as e:  #this e denotes, what error occured in this program, in output screen.
       print("Error",e)
    finally:
      print("Done")   #finally always execute, the program having error or not, the finally keyword always execute.
      
#output:
10
20
ADD:30
Done

  
