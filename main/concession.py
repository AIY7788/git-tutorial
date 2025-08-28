

manu = {"soda": 3.55,
        "potato": 2.50,
        "pizza": 5.66,
        "kitkat":2.40,
        "beer":6.00}


c =[]
total = 0


for key,value in manu.items():
    print(f"{key:10} : ${value:.2f}")


while True :
    food = input("select an item (q to quit) : ").lower()
    if food == "q":
        break
    elif manu.get(food) is not None:
        c.append(food)
    else:
        print("item not found , please select again.")
        
for food in c :
    total += manu.get(food)
    print(food , end=" ")
print()

print(f"total : {total:.2f}")

