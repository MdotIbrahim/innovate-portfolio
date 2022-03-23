# activity 1

welcome = "Welcome to Code Nation."
print(welcome)
welcome_len = len(welcome)
print(welcome_len)

string_to_check = input("Type a word to check the length of: ")
def string_len_even(string):
    string_length = len(string)
    if string_length % 2 == 0:
        print(f"{string} has a string length of {string_length} which is an even number.")
    else:
        print(f"{string} has a string length of {string_length} which is an odd number.")

string_len_even(string_to_check)

#activity 2

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for letter in  alphabet:
    print(letter)

number_position = int(input("Type a number: "))
print(f"The number {number_position} has the position of letter {alphabet[number_position - 1]} in the alphabet.")

#activity 3
