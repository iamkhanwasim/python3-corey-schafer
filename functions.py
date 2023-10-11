# Functions
# Functions allows to put code with a specific purpose into a single unit
# Supports DRY concepts (Dont repeat yourself)
# Think of it like a machine which takes input and produces a result

# Define a function
def hello_func():
    pass

print(hello_func) # prints basic details of functions with memory address
hello_func()    # calling a function


def hello_func():
    print('Hello function!')

hello_func() 
# Output
# Hello function!

# Adding function helper comment

def hello_func():
    "This is function print Hello function!"    # This produces helper comment when functions
                                                # are referenced
    print('Hello function!')


# Return from function

def hello_func():
     return 'Hello function!'

hello_func()    # doesnt produce a result

result = hello_func()   # assigns returning value from function to a variable
print(result)
# Output
# Hello function!

# Attach function to the user defined function
print(hello_func().upper())
# Output
# HELLO FUNCTION!

# Adding parameter to the function
def hello_func(greetings):
    return (f'{greetings}, from function.')

# print(hello_func())     # hello_func() missing 1 required positional argument: 'greetings'
print(hello_func('hi'))
# Output
# hi, from function.

# Parameter with default value
def hello_func(greetings, name = 'You'):
    return (f'{greetings} {name}, from function.')

print(hello_func('hi'))
# Output
# hi You, from function.

print(hello_func('hi', 'Wasim'))
# Output
# hi Wasim, from function.

# *args and **kwargs
# Allows us arbitrary number of positional and keyword arguments
# Names dont have to be args or kwargs, they are just the conventions
def students_info(*args, **kwargs):
    print(args)
    print(kwargs)

students_info('Maths','Art', name='John', Age=23)
# Output
# ('Maths', 'Art') # Tuple with positional parameters
# {'name': 'John', 'Age': 23}   # Dictionary with Keyword parameters

# Function calls using * or **
courses = ['Maths', 'Art']
info = {'name': 'John', 'Age': 23}

students_info(courses, info)    # This doesnt unpacks the arguments
# Output
# (['Maths', 'Art'], {'name': 'John', 'Age': 23})
# {}

students_info(*courses, **info)     #This unpacks the dictionary
# Output
# ('Maths', 'Art')
# {'name': 'John', 'Age': 23}

