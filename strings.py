# Prints Hello world
message = "Hello world"
print(message)

# Escape single quotes
second_message = "Bob's world"
print(second_message)

# Using Escape charater
third_message = 'Bob\'s world'
print(second_message)

# Multi-line string
fourth_message = """Hello world,
this is awesome"""
print(fourth_message)

# Print the length os string
print(len(message))


# Slicing
# Print a character from string at an index
print(message[0])

# Get the substring
print(message[0:4]) 
# 0 is starting point and 4 is the upperbound
# 4th index wont be consider as it is only stopping point
# [0:4] so this would say as get everything starting fr0m index 0 upto but not including index 4


# String methods
print(message.upper()) #turn string to upper case

print(message.count('l')) # counts the occurences of whats passed as argument

print(message.find('o')) #find index of the fisrt occurence

message.replace('world', 'Universe') # replaces the a string/substring with other
#above code wont update message variable. It will return the updated variable
new_message = message.replace('world', 'Universe')
print(new_message)

# Concatenate strings
greetings = "Hello"
name = "John"
message = greetings + ', ' + name + '. Welcome'
print(message)

# Concatenate using Placeholders
message = '{}, {}. Welcome'.format(greetings, name)
print(message)


# Concatenate using f string
message =  f'{greetings}, {name}. Welcome'
print(message)

message =  f'{greetings}, {name.upper()}. Welcome'
print(message)

# Dir method
print(dir(message)) # when passed a variable, dir methods shows all the attributes that have access to variables

# Help method
# print(help(str)) # Gives more information about the type
print(help(str.lower)) # Adding a method name can give specific details of the method associated with the type
