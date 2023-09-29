# int and float types 
number = 3
print(type(number))

number=3.14
print(type(number)) 

# Arithmetic operators
# Addition:       3 + 2
# Subtraction:    3 - 2
# Multiplication: 3 * 2
# Division:       3 / 2
# Floor Division: 3 // 2
# Exponent:       3 ** 2
# Modulus:        3 % 2 
# Modulus in Arithmetic is the remainder when when a number is divided by another number
# *Modulus in Mathematics in particular complex number referes to maginitude or absolute values of a quantity

print ("Addition:", 3+2)
print ("Subtraction:", 3-2)
print ("Multiplication:", 3*2)
print ("Division:", 3/2)
print ("Floor Division:", 3//2)
print ("Exponent:", 3**2)
print ("Modulus:", 3%2)

# Check if number is even or odd
num1 = 345
num2 = 78954
if num1 % 2 == 0:
    print(f"num1 - {num1} is even")
else:
    print(f"num1 - {num1} is odd")

if num2 % 2 == 0:
    print("num2 - {} is even".format(num2))
else:
    print("num2 - {} is odd".format(num2))


# Python follows Arithemetic order of operation
print( 3* (2 + 4))

# Increment and decrements values
num = 1 
num = num +1
print("Increment num: ", num)

num = 1 
num = num +1
print("Decrement num: ", num)

# Shorthand for Increments and decrements
num = 2
num += 1
print("Increment num: ", num)

num = 2
num -=1
print("Decrement num: ", num)


# Built in fuctions for numbers
# abs
# returns absolute value
print (abs(-5))

# round
# returns rounded value
print (round(3.456))
print (round(3.456, 2)) #Specify what how many value to be rounded after decimal


# Comparisions
# Equal:              3 == 2
# Not equal           3 != 2
# Greater than        3 > 2
# Less than           3 < 2
# Greater or equal    3 >= 2
# Lesser or equal     3<= 2


num_1 = '100'
num_2 = '200' 
print(num_1 + num_2) # This joins the string and dont add numbers

# type cast to be added
num_1 = int(num_1)
num_2 = int(num_2)
print(num_1 + num_2) # This adds the 2 numbers
