'''

If else statements
x = int(input("What's x?: "))
y = int(input("What's y?: "))

if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")
'''


'''
#Chaining comparison operators
score = int(input("What is the score?: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print('Grade: B')
elif score >= 70:
    print('Grade: C')
elif score >= 60:
    print('Grade: D')
else:
    print('Grade: F')

    '''

#Modulo

'''
x = int(input("What's x?: "))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")
'''

def main():
    x = int(input("What's x?: "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

main()