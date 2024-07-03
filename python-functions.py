
# Python Functions

# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.
# In Python a function is defined using the def keyword:

# def my_function():
#     print("Hi, Hello world!!")

# my_function()    
 

# function Arguments
# Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses.
# You can add as many arguments as you want, just separate them with a comma.

# def my_function(fname):
#   print(fname + " Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")


# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function,
# add a * before the parameter name in the function definition

# def my_function(*kids):
#   print("The youngest child is " + kids[2])
# my_function("Email", "Tobias", "Linus")  


# Keyword Arguments
# You can also send arguments with the key = value syntax.

# def message(name):
#   print("Hello " + name)
# message("Rinshi")
# message("Favas")
# message("Ashaan")


# def child_fuction(child3, child2, child1):
#   print("The youngest child is " + child1)

# child_fuction(child1="Rasi", child2="Favas", child3="Abu")

# def find_sum(num1, num2):
#     print(num1 + num2)

# find_sum(10, 20)


# How value return 
# def add_num():
#     return 20 + 30

# print(add_num())


# with args
def find_sqare(num):
    return num*num
print(find_sqare(100))