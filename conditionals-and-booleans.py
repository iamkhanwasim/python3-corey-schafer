# Conditionals and Booleans

# Comparisons
# Equal:                  ==
# Not Eqaul               !=
# Greater than            >
# Greater than equal to   >=
# Lesser than             <
# Lesser than equal to    >=
# Object identity         is

# Boolean operations
# and
# or
# not

if True:
    print('condition is true')
# Output
# condition is true


if False:
    print('condition is true')
# Output
# 

# Multiple conditions
language = 'python' #'java'
if language == 'python':
    print('Language is python')
elif language == 'java':
    print('Language is java')
else:
    print('No match')

# Conditions with Boolean operators
# and - or
user ='Admin'
logged_in = False

if user == 'Admin' and logged_in:   # and operator works as logical AND
    print('Admin has logged in.')
elif user == 'Admin' or logged_in:  # or operator works as logical OR
    print('Admin page')
else:
    print('Bad credentials')

# not
if not logged_in:
    print('please login')
else:
    print('Welcome')

# Test if the objects have same memomry ID
# Basically means if they are the same object in memory
# Option 1
a = [1,2,3]
b = [1,2,3]

print(a == b)   #True, because values of a and b are same
print(a is b)   #False, because a and b are 2 different objects in memory

# We can use the id() function to get the ID of the object
print(id(a))
print(id(b))

# Option 2
b = a

print(a == b)   #True, because values of a and b are same
print(a is b)   #True, because a and b share the same ID in memory

# We can use the id() function to get the ID of the object
print(id(a))    #same ID
print(id(b))    #same ID


# False values in Python
# False
# None
# Zero of any numeric type
# An empty sequence: '', [], ()
# An empty mapping: {}

condition = False
condition = None
condition = 0
condition = []
condition = {}
if condition:
    print('Evaluated as True')
else:
    print('Evaluated as False')