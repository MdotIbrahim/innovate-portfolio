# Activity(1)
# Create a program with an input variable that
# encourages the user to enter a number into the
# terminal. If they do, have the program convert this
# into the Int data type, and show me the evidence. If
# they don’t, print a ‘try again’ message.
# Break down this challenge into your own terms, and
# use research to help you solve it. Look back through
# the Python recap and this presentation to see what
# syntax you can use to help you do this.

def user_num():
    user_number = input("\nEnter a number: ")
    try:
        print(type(int(user_number)))
    except:
        print("Try again\n")
        user_num()
user_num()
