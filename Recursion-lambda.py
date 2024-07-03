
# Python Recursion :-
# Oru Function-nte Ullil Aha same function call cheyyunnathine ane Recurtion enn parayunne
# Python also accepts function recursion, which means a defined function can call itself.
# If statement or condition statement use cheyyanam

# def Recursion(n):
#     if n <= 1:
#         return n
#     else:
#         return n + Recursion(n -1)
# a = Recursion(2)
# print(a)      



# Lambda Function (also called anonymous)

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. 

# l = lambda x: x * x
# print(l(5))


# x = lambda a, b: a * b
# print(x(5, 6))



# Filtering even numbers normal fun

# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def even(x):
#     if x % 2 == 0:
#         return x
# f = filter(even, list1)
# print(list(f))  

# # Lambda using in fuction  
# list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# f = filter(lambda x: x % 2 == 0, list2)
# print(list(f))


#example
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))





# Python Arrays
# Python does not have built-in support for Arrays, but Python Lists can be used instead.
# Arrays are used to store multiple values in one single variable:
cars = ["Ford", "Volvo", "BMW"]
# print(cars)
for x in cars:
  print(x)


