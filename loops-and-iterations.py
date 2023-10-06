nums = [1, 2, 3, 4, 5]

# loop through list
for num in nums:
    print(num)
# Output
# 1
# 2
# 3
# 4
# 5


# break and continue
for num in nums:
    if num == 3:
        print("Found!")
        break           # Breaks the loop and stop the further iterations
    print(num)
# Output
# 1
# 2
# Found!

for num in nums:
    if num == 3:
        print("Found 3!")   # Continue stops the current iteration going further and goes to next iteration
        continue        
    print(num)
# Output never prints 3 but goes to other iteration and print 4 and 5 
# 1
# 2
# Found 3!
# 4
# 5

# Loop within a loop
for num in nums:
    for letter in 'abc':
        print(num,letter)
# Output
# 1 a
# 1 b
# 1 c
# 2 a
# 2 b
# 2 c
# 3 a
# 3 b
# 3 c
# 4 a
# 4 b
# 4 c
# 5 a
# 5 b
# 5 c


# Loop for certain number of times
for i in range(10): # range(10) would iterate 10 time | starts from 0-9
    print(i)

# loop through specific range
for i in range(1,11): # Loops 9 times | upper bound is and not including 11 in this case
    print(i)


# While loop
x = 0
while x < 10:   # While loop goes on iterating until the condition turns false
    if x == 5:
        break   # break in while
    print("x =",x)
    x += 1
# Output
# x = 0
# x = 1
# x = 2
# x = 3
# x = 4
