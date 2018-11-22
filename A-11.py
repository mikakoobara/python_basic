height = input("Height(m)? > ")
weight = input("Weight(kg)? > ")

bmi = round(float(weight) / (float(height) * float(height)), 2)

print(f"Your BMI is {bmi}")
