#Object Oriented Programming

#everything is an object in oop. - write cleaner code to maintain easily
# data stored in objects are refFered to as attributes. - WHAT IT HAS
# functions reffered to as methods - WHAT IT DOES

# a class is the blueprint for creating objects...a prototype.

# class Person():
#     def __init__(self): #init is contructor or initaliser
#         self.name = None # creates a new attribute

# better way below:
class Person():
    def __init__(self, person_name, person_age, person_height): #self allows you to make attributes. its a prototype.
        self.name = person_name
        self.age = person_age
        self.height = person_height
    #method we defined
    def set_hair(self, person_hair):
        self.hair = person_hair



# classes use pascals case (all upper case)
# no uses of camel case (first word lower case, rest upper)
# everything else is pretty much snakes case (all lower)
#kebab-case - have dashes

