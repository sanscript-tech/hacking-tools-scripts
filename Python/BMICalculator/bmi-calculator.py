from colorama import Fore, init

init(autoreset=True)

feet, inches = map(int, input(Fore.CYAN + "\nEnter height in feet and inches (example 5'3''): ")[:-2].split("'"))
weight = float(input(Fore.CYAN + "Enter your weight in kgs: "))

height = float(feet*0.3048 + inches*0.0254)
bmi = round(weight / (height*height), 2)
print("\nYour BMI is: ", bmi)

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