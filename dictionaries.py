# Dictionaries
# Key-value pair
# Like physial dictionary where word you are looking is Key and meaning would be Value

# Create a Dictionary
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'ComSci']}
print(student)

# Access a specific value
print(student['name'])

print(student['courses'])

# Key can be of any immutable type
student_test = {'name': 'John', 'age': 25, 'courses': ['Math', 'ComSci'], 1:"test"}
print(student_test[1])

# Get() method
# print(student[1]) #Throws error as key 1 is not available in student dict
print(student.get('name'))
# John

print(student.get(1)) # Return the value for key if key is in the dictionary, else default.
# None

print(student.get(1,"Not found")) # adding default values
# Not found

# Adding key to dictionary
student['phone'] = '555-5555'
print(student)
# {'name': 'John', 'age': 25, 'courses': ['Math', 'ComSci'], 'phone': '555-5555'}

# Update value of dict
student['name']= 'Jane'
print(student)
# {'name': 'Jane', 'age': 25, 'courses': ['Math', 'ComSci'], 'phone': '555-5555'}

# Update method
student.update({'name':'Jane', 'age':28, 'phone':'666-6666'})
print(student)
# {'name': 'Jane', 'age': 28, 'courses': ['Math', 'ComSci'], 'phone': '666-6666'}

# Delete a key
del(student['age'])
print(student)
# {'name': 'Jane', 'courses': ['Math', 'ComSci'], 'phone': '666-6666'}

# Remove the key-value
phone = student.pop('phone')
print(student)
print(phone)
# {'name': 'Jane', 'courses': ['Math', 'ComSci']}
# 666-6666

# Length of dictionary
print(len(student))
# 2


# Get keys and values
print(student.keys())
print(student.values())
print(student.items())
# dict_keys(['name', 'courses'])
# dict_values(['Jane', ['Math', 'ComSci']])
# dict_items([('name', 'Jane'), ('courses', ['Math', 'ComSci'])])

# Loop through dict
for i in student:
    print(i)
# name
# courses

for key, val in student.items():
    print(key, val)
# name Jane
# courses ['Math', 'ComSci']