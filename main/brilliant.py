 





def calculator():
    while True:
        
        num1 = float(input("Enter your first number: "))
        
        
        while True:
            
            operator = input("Enter the operator (+, -, *, /) or 'exit' to quit: ")
            
            if operator == 'exit':
                print("Goodbye!")
                return False 
                
            if operator not in ['+', '-', '*', '/']:
                print("Invalid operator! Please enter one of (+, -, *, /)")
                continue  

            
            num2 = float(input("Enter the next number: "))

            
            if operator == '+':
                num1 += num2
            elif operator == '-':
                num1 -= num2
            elif operator == '*':
                num1 *= num2
            elif operator == '/':
                if num2 != 0:
                    num1 /= num2
                else:
                    print("Error! Division by zero.")
                    continue  

            print("Current result:", num1)

calculator()



