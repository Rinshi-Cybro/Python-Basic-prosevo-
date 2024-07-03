
# Python Classes/Objects

# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.

# 1.CLASS
# Class : Blueprint of Object Collecion 
# eg:- Electronics, Vehicles,   
# Create a Class

# class myclass:
#     x = 5
# print(myclass)


# 2.OBJECTS 
# Object : Member of a class
# Eg:- Tv, laptop, smartphone, car , auto, bus

# Properties(Attributes) 
# Car --> name, color, price

# Methods(Behaviour)
# Car --> start(), run(), stop()

# The __init__() function is called automatically every time the class is being used to create a new object.

class Cars():   # obj
    def __init__(self, name, price, colour):
        self.name = name
        self.price = price
        self.colour = colour

    def start(self):
        print(self.name + "  Engin started")  

car1 = Cars("Toyata Crysta", 100000, "Red")
# change car1 price
car1.price = 500000

car2 = Cars("Maruti Swift", 250000, "Green") 
#change car2 colour 
car2.colour = "Yellow"

car3 = Cars("KIA Seltos", 280000, "Black")     

print(car1.name, car1.price, car1.colour)
print(car2.name, car2.price, car2.colour)
# print(car3.name, car3.price, car3.colour)

# car1.start()
# car2.start()
# car3.start()
        

