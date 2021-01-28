# add numerical lists to assignment
food_inventory = ['pizza', 'pumpkin pie', 'banana', 'apple']
weapons_inventory = ['sword', 'grenade', 'katana']

# print out the food inventory as a numerical list
print("Food inventory:")
# enumarate makes things print out numerically in a list
for i, item in enumerate(food_inventory, 1):
    print(f"{i}. {item}")
print("")

# print out weapons inventory as a numerical list
print("Weapons inventory:")
# enumarate makes things print out numerically in a list
for i, item in enumerate(weapons_inventory, 1):
    print(f"{i}. {item}")
