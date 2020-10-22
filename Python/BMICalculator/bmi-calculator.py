# Colorama helps adding colors to the terminal output

from colorama import Fore, init

init(autoreset=True)

# Getting Height and Weight of User from the input

height = float(input(Fore.CYAN + "\nEnter your height in metres: "))
weight = float(input(Fore.CYAN + "Enter your weight in kgs: "))

# Calculating BMI

bmi = round(weight / (height*height), 2)
print("\nYour BMI is: ", bmi)

# Interpreting the result based on value of BMI

if bmi<15.00:
	print(Fore.RED + "\nYou are very severely underweight!!!\n")
elif bmi<16.00:
	print(Fore.RED + "\nYou are severely underweight!!\n")
elif bmi<18.50:
	print(Fore.BLUE + "\nYou are Underweight!\n")
elif bmi<25.00:
	print(Fore.GREEN + "\nYou are healty!\n")
elif bmi<30.00:
	print(Fore.BLUE + "\nYou are Overweight!\n")
elif bmi<35.00:
	print(Fore.RED + "\nYou are moderately Obese!\n")
elif bmi<40.00:
	print(Fore.RED + "\nYou are severely Obese!!\n")
else:
	print(Fore.RED + "\nYou are very severely Obese!!!\n")