multiplication = True
def table_func(number):
    for n in range(1,13):
        print(f"{number} X {n} = {number * n}")

while multiplication:
    number = int(input("Enter a number: "))
    if number == 999:
        break # ends loop to start next activity - originally used multiplication = False as i always dobut break also ends the loop! Continue works the smae way.
    table_func(number)