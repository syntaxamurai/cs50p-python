num = 3

#to see data type
print(type(num))

'''
Arithmetic Operators:
Addition: +
Subtraction: -
Multiplication: *
Division: /
Floor division: //
Exponent: **
Modulus: % ... If 0, number is even; if 1, number is odd
'''

print(3 * 2 + 1)
print(3 * (2 + 1))
print(3 % 2)
print(num)

#Incrementing a variable 
num += 1
print(num)

num *= 2
print(num)

#Absolute value - removes the negative sign from numbers
print(abs(-37))

#Round - rounds a number to the nearest integer
print(round(4.3))
#To specify how many digits we want to round to
print(round(3.4999, 3))

#Comparisons return a boolean
num_1 = 3
num_2 = 2
print(num_1 == num_2)  #Equal to
print(num_1 != num_2)  #Not equal to
print(num_1 > num_2)   #greater than
print(num_1 <= num_2)  #Less than or equal to

# Integers that are strings
new_num = '100'
new_num_2 = '200'
#How to solve it = casting
new_num = int(new_num)
new_num_2 = int(new_num_2)
print(new_num + new_num_2)