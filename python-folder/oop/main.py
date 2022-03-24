from person import Person, User


liam = Person("Liam", "7", "2'9") # creating an object from a class (blueprint)

print(liam.age)

liam.set_hair("Grey and Curly") # parameters here set the description of the hair.
print(liam.hair)
#change value of attribute
liam.set_hair("Brown and Straight")
print(liam.hair)