# Importing faker library that helps us in generating fake data
from faker import Faker

# Creating instance for faker library
fake = Faker()

# Tanking number of names that user want to generate as input 
n=int(input("Enter how many name you want to generate: "))

# We will be using for loop to generate fake names
for i in range(n):
    print(fake.name())