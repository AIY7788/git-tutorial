
print(f"℃ => ℉ | ℉ => ℃" )
        
while True :
    choice = input("input your choice (℃ or ℉) : ").lower()
    if choice == "c" :

        c = float(input("Input the ℃ : "))

        f =(c * 9/5 + 32)

        print(f"{c} ℃ = {f:.1f} ℉" )

        
    elif choice == "f" : 

        f = float(input("Input the ℉ : "))

        c = ((f - 32) * 5/9)

        print(f"{f} ℉ = {c:.1f} ℃" )
        
    else : 
        
        print("please enter the choice (℃ or ℉)")
        continue

    again = input("Do again ? (Y for Yes / N for No) : ").lower()
    if again != 'y':
        break
        
        

