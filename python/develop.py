import random as r
#? this is a question
#! this is an error
# this is a regular comment
#TODO this needs implementing later
##################################

##################################
#Develop code recap

greeting = "Hello World!" # string
print(greeting)

boolean = False
integer =  1337
empty_variable = None
floating_point = 1337.0000001

print(len("dhfhsldfldsflsdnfsdno"))
print("last letter in this string is"[-1])
#upper, lower, capitalize, count, find

print(r.randint(0,20))
print(round(r.random()*10, 2))

#snake_case is where everything is lowercase
#pascal_case is capital letter. e.g. class Myclass

print(greeting + "Hello again.") # concatenation
num1 = 100
print(f"The number {num1}") # f-string - interpolation

# mathematical operators - +,-,/,*,**,%
# store values instantly - =,*=,-=,+=,/=
num_one = 8
num_one += 7

# == - equal, != - not equal

# and operator - all statements need to be True (or False)
# or operator - either statements need to be True (or False)

fruit_list = ["banana", "grapes", 456]

fruit_tuple = ("carrot", "peas")# can't change data

# for loops

for n in range(0,11, 2):
    print(n)

# while loops
rand_guess = 0
rand_num = r.randint(0,10)
while rand_guess != rand_num:
    rand_guess = r.randint(0,10)
    print(rand_guess)

print(f"You found it! {rand_num}")

i = 1
while i < 6:
    print(i)
    if i == 3:
        print("loop is dead")
        break
    i += 1 

# The continue Statement
# With the continue statement we can stop the current iteration, and continue with the next:
# Example
# Continue to the next iteration if i is 3:
i = 0
while i < 6:
    i += 1
    if i == 3:
        print("I don't like this number")
        continue
    print(i)

for n in range(0, 10): # 9, -1 , -1 teacher code...
    print(n * -1 + 9)

