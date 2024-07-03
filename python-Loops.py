# Python Loops
# Python has two primitive loop commands:
# a) while loops  b)for loops

# 1. while Loop
# With the while loop we can execute a set of statements as long as a condition is true.
# i = 1
# while i < 11:
#   print(i)
#   i += 1


# The break Statement
# With the break statement we can stop the loop even if the while condition is true:  
# i = 1
# while i < 10:
#   print(i)
#   if i == 6:
#     break
#   i += 1

# Continue Statement 
# With the continue statement we can stop the current iteration, and continue with the next:
i = 0
while i < 6:
  i += 1
#   if i == 3:
#     continue
#   print(i)  


# else Statement
# With the else statement we can run a block of code once when the condition no longer is true: 
# i = 1
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("i is no loger less than 6")  



# 2. For Loops
# A for loop is used for iterating over a sequence 
# (that is either a list, a tuple, a dictionary, a set, or a string).
  
# Print each fruit in a fruit list:
fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)


# for x in "Banana":
  # print(x)  


# Break
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x) 
#   if x == "banana":
#     break   
  

# fruits1 = ["apple", "banana", "cherry"]
# for x in fruits1:
#   if x == "banana":
#     break
#   print(x)   



# Start with word
# nameList = ["Rashi", "Rasi", "Favas", "Rahman", "Abu"]
# ab = [word for word in nameList if word.startswith("R")]
# print(ab)


# range() Function
# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, 
# starting from 0 by default, and increments by 1 (by default), and ends at a specified number

# for x in range(11):
#   print(x)



# Else in For Loop
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
# for x in range(6):
#   print(x)
# else:
#   print("Finally finished!")



# The else block will NOT be executed if the loop is stopped by a break statement.  
# eg:-
# for x in range(6):
#   if x == 3: break
#   print(x)
# else:
#   print("Finally finished!")



# Nested Loops
# A nested loop is a loop inside a loop.
# The "inner loop" will be executed one time for each iteration of the "outer loop":

# colr = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in colr:
#   for y in fruits:
#     print(x, y)


# Print each character in a string using For loop
string = "Hello World"
# for i in string:
#   print(i)

# index via   
# text = "Hello World"
# for i in text[0:5]:
#   print(i)

# Using List
# List1 = ["Car", "Bus", "Bike"]  
# for i in List1:
#   print(i)


# for loop using range()
for i in range(6):
  print(i)
  