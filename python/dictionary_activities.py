# Activity(2)
# Make a countries dictionary to represent these
# countries and their capital cities - United Kingdom,
# France, Germany, Spain and Italy.
# Now use the .setdefault() method to add any 2
# more countries and capitals of your choice
# Print all items using a method previously seen before.
# Make a note of which method you prefer, and why.
# You’ve had a change of heart - now update all the
# values with the main language spoken in the
# countries instead of capitals

countries = {
    "United Kingdom": ["London", "English"], # i made the value into a list to add both capital and language instead of changing the value
    "France": ["Paris", "French"],
    "Germany": ["Berlin", "German"],
    "Spain": ["Madrid","Spanish"],
    "Italy": ["Rome", "Italian"]
}

countries.setdefault("Russia", "Moscow")
countries.setdefault("Japan", "Tokyo")
print(countries)
print(list(countries.items()))

print(countries["France"][1])
