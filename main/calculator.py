

num1 = float(input("Enter the first number : "))
calculat =input ("Please enter an operator (+, -, *, /) : ")
num2 = float(input("Enter the second number : "))


while calculat != '+' and calculat != '-' and calculat != '*' and calculat != '/':
    print("Invalid operator! Please enter one of (+, -, *, /)")
    calculat = input("Enter the operator (+, -, *, /): ")


if calculat == '+':
    result = num1 + num2
    
elif calculat =='-':
    result = num1 - num2
    
elif calculat =='*':
    result = num1 * num2
    
elif calculat =='/':
    while num2 == 0 :
        print ("the second number mustn't be zero ")
        num2 = float(input("Enter the second number : "))
    result = num1 / num2
    
print(f"{num1} {calculat} {num2} : {result}")