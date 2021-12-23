height = float(input("enter the height"))
weight = float(input("enter the weight"))
bmi = round(weight / height ** 2)
print(bmi)

if bmi < 18.5:
    print("underwight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("overweight")
elif bmi < 35:
    print("obese")
else:
    print("clinically obese")