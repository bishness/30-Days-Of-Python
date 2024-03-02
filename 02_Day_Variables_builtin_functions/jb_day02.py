#Exercises: Level 1
#Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
#created jb_day2.py

# Write a python comment saying 'Day 2: 30 Days of python programming'
# 'Day 2: 30 Days of Python programming'


# Declare a first name variable and assign a value to it
first_name = 'jeremy'

# Declare a last name variable and assign a value to it
last_name = 'bishops'

# Declare a full name variable and assign a value to it
full_name = first_name + ' ' + last_name

# Declare a country variable and assign a value to it
country = 'USA'

# Declare a city variable and assign a value to it
city = 'Hamilton'

# Declare an age variable and assign a value to it
age = 46

# Declare a year variable and assign a value to it
year = 2024

# Declare a variable is_married and assign a value to it
is_married = True

# Declare a variable is_true and assign a value to it
is_true = True

# Declare a variable is_light_on and assign a value to it
is_light_on = False

# Declare multiple variable on one line
has_kids, likes_tech, daily_water = True, True, 30


# Exercises: Level 2
# Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(last_name))
print(len(full_name))
print(type(daily_water))

# Using the len() built-in function, find the length of your first name
print(len(first_name))

# Compare the length of your first name and your last name
comp_name = len(first_name) == len(last_name)
print(comp_name)

# Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

# - Add num_one and num_two and assign the value to a variable total
total = num_one + num_two

# - Subtract num_two from num_one and assign the value to a variable diff
diff = num_two - num_one

# - Multiply num_two and num_one and assign the value to a variable product
product = num_two * num_one
# - Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two

# - Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one

# - Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two

# - Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_dividion = num_one // num_two

# The radius of a circle is 30 meters.
p = 3.14
r = 30
# - Calculate the area of a circle and assign the value to a variable name of area_of_circle
area_of_circle = p*r**2
print(area_of_circle)

# - Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2*p*r
print(circum_of_circle)

# - Take radius as user input and calculate the area.
r = int(input('enter radius value: '))
user_area_circle = p*r**2
print(user_area_circle)

# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
country = input('Enter your country: ')
age = input('Enter your age: ')

print(first_name,last_name,country,age)

# Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
print(help('keywords'))
