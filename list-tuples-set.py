#List, Tuples, and Sets


# List
# Mutable
courses = ['History','Math','Physics','CompSci']

# Print course at index 0
print(courses[0]) 

# Print course at last index
print(courses[-1]) 

# Get range
print(courses[0:3]) 

# Get range from start to 2
print(courses[:3])

# Add element to list
courses.append('Art')
print(courses)

# Insert element at specific loaction
courses.insert(1, 'Geography')
print(courses)

# Insert elements to the list
courses.extend(['Education', 'Medicine'])
print(courses)

# Remove elements from List
courses.remove('Math')
print(courses)

# Remove last value from the list
# This is useful when we use the List as Stack or Queue
courses.pop()
print(courses)

# We can grab the popped out value in a variable
popped_value = courses.pop()
print(popped_value)
print(courses)

# Pop out at spefice index
val = courses.pop(2)
print(val)
print(courses)

# Reverse a List
courses.reverse()
print(courses)

# Sort the list
# courses.sort()
# print(courses)

#Descending order
nums = [3,6,2,8,5,3,9]
nums.sort(reverse=True)
print(nums)

# Sorted function
sorted_courses = sorted(courses)
print(sorted_courses)

# Min , Max, and Sum
print(min(nums))
print(max(nums))
print(sum(nums))

# Index method
print(courses.index('CompSci'))

# Trying to find index of element not in the list
# Throws error
# ValueError: 'Education' is not in list
# print(courses.index('Education'))

# To check if element is present in the list
print('Art' in courses)

# Print each item in the List using for loop
for item in (courses):
    print(item)


# Using enumerate function
for index, item in enumerate(courses):
    print(index,item)

# Convert list to string
course_str = ' ,'.join(courses)
print(course_str)

# Convert string to List
new_list = course_str.split(' ,')
print(new_list)

# What are Mutable objects
list_1 = ['History','Math','Physics','ComSci']
list_2 =  list_1

print('list_1',list_1)
print('list_2',list_2)

list_1.append('Art')

print('list_1',list_1)
print('list_2',list_2)


# Tuples
# Immutable
tuple_1 = ('History','Math','Physics','ComSci')
tuple_2 = tuple_1

print('tuple_1',tuple_1)
print('tuple_2',tuple_2)

# tuple_1[0] = 'Art' # Throws error: TypeError: 'tuple' object does not support item assignment
# We can change or append or insert anything in Tuple because they are immutable


tuple_3 = ('History','Math','Physics','ComSci')
tuple_4 = ('History','Math','Physics','ComSci')
list_3 = ['History', 'Math', 'Physics', 'ComSci', 'Art']

import sys
str1="list_3"
str2="list_3"
str1 = sys.intern("hello")
str2 = sys.intern("hello")
print(str1)
print(str2)
print(str1 is str2)
# print(list_1 == list_3)

# If you need something that you can modify then use 'List'
# If you need something that you can access and loop through then use 'Tuples'


# Sets
# Unorderd list of distinct values
cs_courses = {'History','Math','Physics','ComSci'}
print(cs_courses)
# order would be different in putput to what was assigned 

# Sets removes duplicates
cs_courses = {'History','Math','Physics','ComSci','Math'}
print(cs_courses)

# Set methods
# Intersection
art_courses = {'History','Math','Art','Design'}
print(art_courses)

print('inter', cs_courses.intersection(art_courses))

# Difference
print('diff',cs_courses.difference(art_courses))

# # Unions
print(cs_courses.union(art_courses))


# Create empty List, Tuples and Set
empty_list = []
empty_list = list()

empty_tuple = ()
empty_tuple = tuple()

empty_set = {} # this wont create set but a Dictionary
print(type(empty_set))

empty_set = set()
print(type(empty_set))
