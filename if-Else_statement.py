# If statement
# An "if statement" is written by using the if keyword

a = 33
b = 200
# if b > a:
#   print("b is greater than a")


# Elif statement  
a = 33
b = 39
# if b > a:
#   print("b is greater than a")  
# elif a == b:
#   print("a and b are equal")


# Else
# The else keyword catches anything which isn't caught by the preceding conditions.  
a = 200
b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# else:
#   print("a is greater than b")

c = 0
if c > 0:
  print("It is a Positive number")
elif c < 0:
  print("It is a Negative number")
else:
  print("it is a Zero")



# Short Hand If
# This technique is known as Ternary Operators, or Conditional Expressions.
# if a > b: print("a is greater than b")

a = 2
b = 330
# print("A") if a > b else print("B")


# and
# The and keyword is a logical operator, and is used to combine conditional statements:
a = 200
b = 33
c = 500
# if a > b and c > a:
#   print("Both conditions are True")


# Or
# The or keyword is a logical operator, and is used to combine conditional statements: 
a = 200
b = 33
c = 500
# if a > b or a > c:
#   print("At least one of the conditions is True") 


# Not
# The not keyword is a logical operator, and is used to reverse the result of the conditional statement:  
a = 33
b = 200
# if not a > b:
#   print("a is NOT greater than b")



# Nested If
# You can have if statements inside if statements, this is called nested if statements. 
# x = 41
# if x > 10:
#   print("Above ten,")
#   if x > 20:
#     print("and also above 20!")
#   else:
#     print("but not above 20.") 


# The pass Statement
# if statements cannot be empty, but if you for some reason have an if statement with no content,
# put in the pass statement to avoid getting an error. 
a = 33
b = 200
if b > a:
  pass   