multiplication = True
def table_func(number):
    for n in range(1,13):
        print(f"{number} X {n} = {number * n}")

while multiplication:
    number = int(input("Enter a number: "))
    if number == 999:
        break
    table_func(number)
