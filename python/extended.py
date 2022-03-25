# casting

num = int("7")
flt = float("3.14159")
str = str(231)

print(7*num)
print(flt**3)
print(str, "is a number")

# truthy and falsy

# falsy is "", 0 and 0.0. Everything else is truthy.

#try and except - used to display errors that we're accounting for. The original way would be to use while loop and if statements. try, except can reduce the logic and restructuring of code.
def add_up():
    num1 = input("Number 1: ")
    num2 = input("Number 2: ")
    try:
        print((int(num1) + int(num2)))
    except:
        print("\nERROR. TYPE NUMERICAL VALUES ONLY.\n")
        add_up()

add_up()

#global and lcocal scopes

coffee_is_grinding = False # global variable
def press_grind_beans():  
    global coffee_is_grinding # no longer local
    if coffee_is_grinding: 
        print("Stopping the grind")  
        coffee_is_grinding = False 
    else: 
        print("Grinding is about to begin") 
        coffee_is_grinding = True 
press_grind_beans() 
press_grind_beans()