weight = float(input("insert your weight in kg:"))
height = float(input("insert your height in metre:"))
bmi_formular = weight/(height*height)
result = f"your bmi is {bmi_formular:.2f}"
print(result)


