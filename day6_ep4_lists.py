courses = ['History', 'Maths', 'Physics', 'CompSci']
print(courses)

#To see length of list
print(len(courses))

#To access values in the list individually - last item
print(courses[-1])

#To access range of values - not including the last index (slicing)
print(courses[:2])

#List methods
#Append - Adds item to end of list
courses.append('Art')
print(courses)

#Insert - Adds item to specific area
courses.insert(0, 'Law')
print(courses)

#Extend - Add multiple individual values at the end 
courses_2 = ['Arts', 'Education']
courses.extend(courses_2)
print(courses)

#Remove values
#Using remove
courses.remove('Art')
print(courses)
#using pop - removes last item in the list
popped = courses.pop()
print(popped)
print(courses)

#Reversing the list as is
courses.reverse()
print(courses)

#Sorting the list - Sorts the list items alphabetically, ascending order
nums = [1, 4, 3, 23, 34, 21, 1]
courses.sort()
nums.sort()
print(courses)
print(nums)

#Sorting the list - Sorts the list items alphabetically, descending order
nums = [1, 4, 3, 23, 34, 21, 1]
courses.sort(reverse=True)
nums.sort(reverse=True)
print(courses)
print(nums)

#Sorting without altering original list
names = ["Justin", "Brian", "Kevin", "Tevin", "Kip"]
new_names = sorted(names)
print(names)
print(new_names)

#Minimum value
print(min(nums))

#maximum value
print(max(nums))

#sum of values
print(sum(nums))

#Find INDEX of values in a list
print(names.index('Tevin'))

#Check if value is in list, return boolean
print('Justin' in names)

#Loop through each values in the loop
for name in names:
    print(name)
#To check which index we are looping at
for index, name in enumerate(names, start=1):
    print(index, name)

#To turn a list into a string of comma separated values
name_str = ' - '.join(names)
print(name_str)

#Turn a string to a list
name_list = name_str.split(' - ')
print(name_list)