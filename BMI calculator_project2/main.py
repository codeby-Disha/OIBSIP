# BMI Calculator 

try:
    
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))

    
    if height <= 0:
        print("Height must be greater than 0")
    else:
        
        bmi = weight / (height ** 2)

        
        print("Your BMI is:", round(bmi, 2))

       
        if bmi < 18.5:
            print("Category: Underweight")
        elif bmi < 25:
            print("Category: Normal weight")
        elif bmi < 30:
            print("Category: Overweight")
        else:
            print("Category: Obese")

except ValueError:
    print("Please enter valid numeric values for weight and height.")

except ZeroDivisionError:
    print("Height cannot be zero.")

except Exception as e:
    print("An unexpected error occurred:", e)
