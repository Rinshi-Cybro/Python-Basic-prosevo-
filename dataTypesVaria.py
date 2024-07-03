
#<============================= PYTHON VARAIABLS AND DATATYPES ===========================>

# Naming Variables
# 1. Letter or underscore(_)
# 2. Cannot start with number
# 3. Alphanumeric ( A-Z, a-z, 0-9, _ )
# 4. Case sensitive (name NAME, Name)

# Data types (int, string, float, complex, boolean, Data collection(list, tuple, set, dict))
# 1. Integer
b = 10

# 2. string
name = 'Favas'

# 3. float
num = 15.5

# 4. complex
x = 10j

# 5. Boolean
python = True
java = False

# print(type(a))
# print(type(name))
# print(type(num))
# print(type(x))
# print(type(python))
# print(type(java))

# 6. List
x = ["apple", "banana", "cherry"]
# print(x)

# 7. Tuple
b = ("apple", "banana", "cherry") 
# print(b)


# 8. Dictionary
c = {"name" : "John", "age" : 36} 
# print(c)

#<===============================================================================================================>

# Assing Multiple values
x,y,z =  "Orange", "Banana", "Apple"
# print(x)
# print(y)
# print(z)
# print(x,y,z)


# Unpack a collection
""" If you have a collection of values in a list, tuple etc. 
    Python allows you to extract the values into variables.
    This is called unpacking """

fruits = ["Apple", "Banana", "Cherry"]
a,b,c = fruits
# print(a)
# print(b)
# print(c)


# Output Variable
# In the print() function, you output multiple variables, separated by a comma
q = "Python"
r = "is"
s = "Powerfull"
# print(q, r, s)
# print(q + r + s)

x = 5
y = 10
# print(x + y)


# Global Variable
# Variables that are created outside of a function are known as global variables
# x = "Awesome"

# def myFun():
#     print("Python is " + x)
# myFun()    



# To change the value of a global variable inside a function,
#  refer to the variable by using the global keyword
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

# print("Python is " + x)


#<-====================================================================================================================->

# Convert from one type to another
x = 1                              # int
y = 2.8                            # float
z = 1j                             # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

# print(a)
# print(b)
# print(c)


#<-======================================================================================================================================->

#<-------------------- STRING METHODS ------------------------>
# 1. Strings are Arrays
# Get the character at position 1
a = "Hello, World!"
# print(a[4])


# 2. Looping string
# for x in "Banana":
#   print(x)


# 3. Length of a string
ab = "Hello, World"
# print(len(ab)) 


# 4. Check String (use the keyword 'in')
txt = "The best things in life are free!"
# print("free" in txt)


# Use it in an if statement
# txt = "My name is Favas!"
# if "Favas" in txt:
#   print("Yes, 'Favas' is present.")


# 5. Check if NOT
txt = "The best things in life are free!"
# print("expensive" not in txt)


# 6. String Slicing
b = "Hello, World!"
# print(b[2:5])
# starting
b = "Hello, World!"
# print(b[:5])
# ending
b = "Hello, World!"
# print(b[2:])
# Negative Indexing
b = "Hello, World!"
# print(b[-5:-2])


# 7. Upper Case
a = "hello, world!"
# print(a.upper())


# 8. Lower case
a = "HELLO, WORLD!"
# print(a.lower())


# 9. Remove Whitespace
a = " Hello, World! "
# print(a.strip()) # returns "Hello, World!"


# 10. Replace String
a = "Hi, Hello!"
# print(a.replace("Hi", "Hi Rasi"))


# 11. Split String (The split() method returns a list where the text)
x = "Hello, World!"
# print(x.split(","))    # returns ['Hello', ' World!']


# 12. String Concatenation
b = "Hello"
c = "World"
a = b + c
# print(a)


# 13. String Format
# F-Strings
# To specify a string as an f-string, simply put an f in front of the string literal, 
# and add curly brackets {} as placeholders for variables and other operations.
age = 26
txt = f"My name is John, I am {age}"
# print(txt)


#<-==========================================================================================================================================->

#<---------------------------  Python Operators ------------------------->
# 1. Arithmetic operators

# Addition :-
x = 10
y = 5
# print(x + y)

# Subtraction :-

a = 5
b = 2
# print(a - b)

# Multiplication :-
y = 10
z = 5
# print(y * z)

# Division :-
p = 20
r = 2
# print(p / r)

# Modulus :-
x = 20
y = 2
# print(x % y)

# Exponentiation :-
x = 5
y = 3
# print(x ** y) #same as 5*5*5

# Floor division :-
x = 15
y = 2
# print(x // y)   #the floor division // rounds the result down to the nearest whole number

#<----------------------------------------------------------------------------------------------------------------------------------------------->

# 2. Comparison Operators
# Equal
x = 5
y = 5
# print(x == y)   # returns False because 5 is not equal to 3

# Not equal
x = 5
y = 3
# print(x != y)  # returns True because 5 is not equal to 3

# Greater than
x = 10
y = 4
# print(x > y)  # returns True because 10 is greater than 4


# Less than
x = 5
y = 3
# print(x < y)  # returns False because 5 is not less than 3


#	Greater than or equal to
x = 5
y = 3
# print(x >= y) # returns True because five is greater, or equal, to 3


# Less than or equal to
x = 5
y = 3
# print(x <= y)  # returns False because 5 is neither less than or equal to 3

#<----------------------------------------------------------------------------------------------------------------------------------------------->

# 3. Logical Operators
# and Operators (Returns True if both statements are true)
x = 5
# print(x > 3 and x < 10)   # returns True because 5 is greater than 3 AND 5 is less than 10


# or Operators (Returns True if one of the statements is true)
x = 5
# print(x > 3 or x < 4)   # returns True because one of the conditions are true (5 is greater than 3, but 5 is not less than 4)


# not (Reverse the result, returns False if the result is true)
x = 5
# print(not(x > 3 and x < 10))   # returns False because not is used to reverse the result


#<----------------------------------------------------------------------------------------------------------------------------------------------->

# 4. Assignment Operators
# x = 5      	 x = 5
x = 5
# print(x)


# x += 3	     x = x + 3
x = 5
x += 3
# print(x)


# x -= 3	     x = x - 3
x = 5
x -= 3
# print(x)


# x *= 3	    x = x * 3
x = 5
x *= 3
# print(x)


#	x /= 3    	x = x / 3
x = 5
x /= 3
# print(x)

# x %= 3	   x = x % 3
x = 5
x%=3
# print(x)

#	x //= 3	   x = x // 3
x = 5
x//=3
# print(x)


#	x **= 3	  x = x ** 3
x = 5
x **= 3
# print(x)



# 5. Bitwise Operators
#	AND	(Sets each bit to 1 if both bits are 1)	            x & y
# OR	(Sets each bit to 1 if one of two bits is 1)	      x | y
# XOR	(Sets each bit to 1 if only one of two bits is 1) 	x ^ y
# NOT	 (Inverts all the bits)	                             ~x

#<-==========================================================================================================================================->















