monthlyExpense = [
    {"January": 2200},
    {"February": 2350},
    {"March": 2600},
    {"April": 2130},
    {"May": 2190},
]

# arrays access
print("------------------------\nExercises:\n------------------------\n1:")

extra = monthlyExpense[1]["February"] - monthlyExpense[0]["January"]
print(f"In Feb, you spent {extra} extra in comparison to Jan.\n")

print("2:")
firstQuarter = (
    monthlyExpense[1]["February"]
    + monthlyExpense[0]["January"]
    + monthlyExpense[2]["March"]
)
print(f"Total expense of first quarter: {firstQuarter}\n")


print("4:")
monthlyExpense.append({"June": 1980})
print(f"June appended and the total spent was: {monthlyExpense[-1]["June"]}\n")

print("5:")
print(f"April before refund: {monthlyExpense[3]["April"]}")
monthlyExpense[3]["April"] -= 200
print(f"April after refund: {monthlyExpense[3]["April"]}\n")

# list operations
heros = ["spider man", "thor", "hulk", "iron man", "captain america"]
print("------------------------\nExercises 2:\n------------------------\n1:")

print(f"Lenght of list: {len(heros)}")
heros.append("Black Panther")
print(heros[-1])
heros.remove("Black Panther")
heros.insert(3, "Black Panther")
heros[1:3] = ["Doctor Strange"]
heros.sort()
print(heros)
