# Python Collections (Arrays)
# a)List['', '']   b)Tuple('', '')   c)Set{'', ''}   d)Dictionary{'':''} 

# a) Lists '[ ]'
# Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used to store collections of data
# List items are ordered, changeable, and allow duplicate values.

mylist = ["apple", "banana", "cherry"]
# print(mylist)
# print(type(mylist))

# List Allow Duplicate value
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
# print(thislist) 

# List Length
thislist = ["apple", "banana", "cherry"]
# print(len(thislist))

# List count
this_mylist = ["apple", "banana", "cherry", "apple", "cherry"]
# print(this_mylist.count("apple"))

# Change Item Value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
# print(thislist)

# Insert new Items(The insert() method inserts an item at the specified index)
thislist = ["rasi", "favas", "abu"]
thislist.insert(2, "sahal")
# print(thislist) 


# List Data types
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

# Using the list() constructor to make a List
thislist = list(("apple", "banana", "cherry"))
# print(thislist)


# Append Items (Using the append() method to append an item)
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
# print(thislist)

# Insert Items(To insert a list item at a specified index, use the insert() method)
thislist1 = ["apple", "banana", "cherry"]
thislist1.insert(1, "orange")
# print(thislist1)

# Extend List(To append elements from another list to the current list, use the extend() method.)
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
# print(thislist)

# Remove Specified Item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
# print(thislist)

# Remove Specified Index (The pop() method removes the specified index)
thislist = ["mango", "pineapple", "papaya"]
thislist.pop(1)
# print(thislist)

# The del keyword also removes the specified index
thislist = ["apple", "banana", "cherry"]
del thislist[0]
# print(thislist)

# clear th list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
# print(thislist)

# For loop
# my_list1 = ["apple", "banana", "cherry"]
# for x in my_list1:
#   print(x)


# While Loop  
list1 = ["apple", "banana", "cherry"]
i = 0
while i < len(list1):
#   print(list1[i])
  i = i + 1


# Sort List
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
# print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
# print(thislist)


# Sort Descending
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
# print(thislist)

# Copy list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
# print(mylist)


# Start with word
nameList = ["Rashi", "Rasi", "Favas", "Rahman", "Abu"]
ab = [word for word in nameList if word.startswith("R")]
# print(ab)


# Join Two Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
# print(list3)


# 1: Removing duplicates from a list
# my_list = [1, 2, 2, 3, 4, 4, 5]
# unique_list = list(set(my_list))
# print(unique_list)                  # Output: [1, 2, 3, 4, 5]

# 2: Finding the intersection of two lists
# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]
# intersection = list(set(list1) & set(list2))
# print(intersection)  # Output: [3, 4]


#<----------------------------------------------------------------------------------------------------------------------------->

# b) Tuples '( )'

# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets '( )'.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

thistuple = ("apple", "banana", "cherry")
# print(thistuple)


thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
# print(thistuple)

thistuple = ("apple", "banana", "cherry")
# print(thistuple[1])

# Range of Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[2:5])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[:4])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[2:])

# Check if Item Exists
thistuple = ("apple", "banana", "cherry")
# if "apple" in thistuple:
  # print("Yes, 'apple' is in the fruits tuple")


# Once a tuple is created, you cannot change its values. Tuples are unchangeable,
# or immutable as it also is called 
# But there is a workaround. You can convert the tuple into a list, change the list,
# and convert the list back into a tuple. 

x = ("Apple", "Banana", "Cherry")
y = list(x)
# print(y)
y[1] = "Mango"
# print(y)
x = tuple(y)
# print(x)


# Add Items
# Since tuples are immutable, they do not have a built-in append() method,
# but there are other ways to add items to a tuple
myTuple = ("Apple", "Cherri", "Banana")
a = list(myTuple)
a.append("Mango")
myTuple = tuple(a)
# print(myTuple)

# Remove item
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
# print(thistuple)


# Problem 1: Converting a list to a tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
# print(my_tuple)


# Unpacking a Tuple
# Allowed to extract the values back into variables is called Unpacking a Tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
# print(green)
# print(yellow)
# print(red)

my_tuple = (1, 2, 3)
a, b, c = my_tuple
# print(a, b, c) 


# Using Asterisk '*'
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
# print(green)
# print(yellow)
# print(red)

# using for Loop
thistuple = ("apple", "banana", "cherry")
# for x in thistuple:
  # print(x)


# Join Two Tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
# print(tuple3)

#<----------------------------------------------------------------------------------------------------------------------------->

# c) Sets '{ }'

# Sets are used to store multiple items in a single variable.
# A set is a collection which is unordered, unchangeable*, and unindexed
# Set items are unchangeable, but you can remove items and add new items
# Duplicates Not Allowed
thisset = {"Favas", "Shan", "Abu"}
# print(thisset)

# The values True and 1 are considered the same value in sets, and are treated as duplicates
thisset = {"apple", "banana", "cherry", True, 1, 2}
# print(thisset)

# Length of a Set
thisset = {"apple", "banana", "cherry"}
# print(len(thisset))


# data type 'set'
myset = {"apple", "banana", "cherry"}
# print(type(myset))


# Add Set Items
# To add one item to a set use the add() method.
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
# print(thisset)

# To add items from another set into the current set, use the update() method.
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
# print(thisset)

# Remove items
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
# print(thisset)


# Finding the union of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
# print(union_set)


# Checking for subset
set1 = {1, 2, 3}
set2 = {1, 2}
# print(set2.issubset(set1))

# If the item to remove does not exist, remove() will raise an error.
# using the discard() method
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
# print(thisset)


# Looping 
thisset = {"apple", "banana", "cherry"}
# for x in thisset:
  # print(x)


# Union
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1 | set2 | set3 |set4
# print(myset)


# Update set
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
# print(set1)

# Intersection
# The intersection() method will return a new set,
# that only contains the items that are present in both sets.
set1 = {"apple", "banana", "cherry", "microsoft"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
# print(set3)



#<----------------------------------------------------------------------------------------------------------------------------->

# d) Dictionaries '{"" : ""}'

# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# print(thisdict)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# print(thisdict["brand"])


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]


# get items
# Get the value of the "model" key
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")
# print(x)



car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["color"] = "red"
# print(x) 


# Change items
uni_dict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# print(uni_dict)
# uni_dict["year"] = 2024
# print(uni_dict)


# Update dic
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
# print(thisdict)


# Remove dic
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
# print(thisdict)   

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
# print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
# print(thisdict)   
 

# for Loop dic
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# for x, y in thisdict.items():
#   print(x, y)


thisdict1 =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# for x in thisdict1.values():
#   print(x)  


thisdict2 =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# for x in thisdict2.keys():
#   print(x)    


# Nested Dictionaries
# A dictionary can contain dictionaries, this is called nested dictionaries.
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)


# 1: Adding and updating dictionary entries
my_dict = {'a': 1, 'b': 2}
my_dict['c'] = 3  # Adding new entry
my_dict['a'] = 10  # Updating existing entry
# print(my_dict)

# 2: Iterating over dictionary keys and values
dic1 = {'a':1, 'b':2, 'c':3}
# for key, value in dic1.items():
  # print(f"Key: {key}, Value: {value}")


# 3: Merging two dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = {**dict1, **dict2}
# print(merged_dict)


new_dict = {
  "name": "Favas",
  "email":"favi@gmail.com",
  "phone": 2390753489
}
a = new_dict.get("email")
print(new_dict)