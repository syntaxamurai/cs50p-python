student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
# student['phone'] = '0712345678' #add a key value to the dictionary
# student['name'] = 'Jane' #updates 1 value

#To update several value
student.update({'name': 'Jay', 'age': 26, 'phone': '0712345678'})

#To delete a key and its value
# del student['age']

#To remove and return the value
age = student.pop('age')

#To check the length of a dictionary
print(len(student))

#To see only the keys
print(student.keys())

#To see only the values
print(student.values())

#To see all the items in the dictionary
print(student.items())

# To loop through the dictionary
for key, value in student.items():
    print(key, value)

print(student)
print(age)
print(student['name']) #prints a specific value
print(student['courses'])
# print(student['phone']) #prints error message
# print(student.get('phone', 'Not Available')) #returns string error message
print(student.get('phone', 'Not Available'))  # returns the updated value of phone