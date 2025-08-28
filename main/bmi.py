
def calculate_bmi(weight , height): 
    return weight / (height ** 2)

weight = float(input ("Enter your weight : "))
height = float(input ("Enter your height : "))

bmi = calculate_bmi(weight ,height)

print(f"your BMI is {bmi:.2f}")