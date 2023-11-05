#Python Programming Internship - Oasis InfoByte 
#Project : BMI Calculator
#https://www.nhlbi.nih.gov/health/educational/lose_wt/BMI/bmi_dis.htm
#nhlbi = National Heart, Lung, and Blood Institute
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal (Healthy) Weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def get_valid_input(prompt):
    while True:
        user_input = input(prompt)
        if not user_input:
            print("Input cannot be empty. Please try again.")
            continue

        try:
            value = float(user_input)
            if value <= 0:
                print("Input must be a positive number. Please try again.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    print("BMI Calculator")
    weight = get_valid_input("Enter your weight in kilograms: ")
    height = get_valid_input("Enter your height in meters: ")

    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)

    print(f"Your BMI is: {bmi:.2f}")
    print(f"Classification: {category}")

if __name__ == "__main__":
    main()
