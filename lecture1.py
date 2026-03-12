'''
x = int(input("What's x?: "))
y = int(input("What's y?: "))

if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")
'''


score = int(input("What is the score?: "))

if 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score < 90:
    print('Grade: B')
elif 70 <= score < 80:
    print('Grade: C')
elif 60 <= score < 70:
    print('Grade: D')
else:
    print('Grade: F')