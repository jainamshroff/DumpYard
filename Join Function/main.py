# Join Function In Python
# Its joins all the elements of the list with something

list1 = ["John", "Cena", "Randy", "Orton", "Sheamus", "Khali", "Jinder", "Mahal"]

for item in list1:
    print(item, "and ", end="")

a = ", ".join(list1)

print("\nOther WWE Superstars")
print(a)